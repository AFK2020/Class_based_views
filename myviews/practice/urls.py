from .views import TaskList, TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,CustomLogoutView, RegisterPage
from django.contrib.auth.views import LogoutView

from django.urls import path


urlpatterns = [
    path('login/',CustomLoginView.as_view(), name= 'login'),
    path('logout/',CustomLogoutView.as_view(), name= 'logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
