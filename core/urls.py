from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/detail', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/create', views.TaskCreateView.as_view(), name='task_form'),
]