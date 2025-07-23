from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from core.forms import TaskForm
from core.models import Task

class TaskListView(ListView):
    model = Task
    template_name = "track/task_list.html"
    context_object_name = "task_list"

class TaskDetailView(DetailView):
    model = Task
    template_name= "track/task_detail.html"

class TaskCreateView(CreateView):
    model = Task
    #fields = ['title', 'description', 'status', 'priority', 'deadline']
    template_name = 'track/task_form.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)