from .views import TaskList, TaskDetail,TaskCreate
#,TaskDelete,TaskUpdate
from django.urls import path


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
#     path('task-update/<str:pk>/', TaskUpdate.as_view(), name='task-update'),
#     path('task-delete/<str:pk>/', TaskDelete.as_view(), name='task-delete'),
]
