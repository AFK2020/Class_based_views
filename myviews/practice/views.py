from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.shortcuts import redirect

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'practice/login.html'
    redirect_authenticated_user = True # if user is authenticated then don't bring it back to this page

    def get_success_url(self):
        return reverse_lazy('tasks')


class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post', 'options']
    next_page = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)  # Log out the user
        return redirect('login')


class RegisterPage(FormView):
    template_name = 'practice/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage,self).get(*args,**kwargs)


    


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'practice/taskdetail.html'


class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url =reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super(TaskCreate,self).form_valid(form)
        return response

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url =reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    