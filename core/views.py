from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.models import Task

class TaskListView(ListView):
    model = Task
    template_name = "track/task_list.html"

class TaskDetailView(DetailView):
    model = Task
    template_name= "track/task_detail.html"