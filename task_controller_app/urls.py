from django.contrib import admin
from django.urls import path
from task_controller_app.views import TaskListView, TaskCreateView, TaskDetailView, TaskDeleteView, TaskUpdateView, TaskCompleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('task/complete/<int:pk>', TaskCompleteView.as_view(), name='task_complete')
]
