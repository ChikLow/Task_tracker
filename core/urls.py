from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    #path('task/<int:pk>/detail', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/create', views.TaskCreateView.as_view(), name='task_form'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', views.TaskDeleteView.as_view(), name='task_delete'),
]