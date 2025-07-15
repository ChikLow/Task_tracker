from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS_CHOICES = [
        ("todo", "To do"),
        ("in_progress", "In progress"),
        ("done", "Done")
    ]

    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Middle"),
        ("H", "High"),
        ("C", "Critical")
    ]

    title = models.CharField(max_length=100, verbose_name="name")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="name")
    description = models.TextField(null=True, blank=True, verbose_name="name")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo", verbose_name="name")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="M", verbose_name="name")
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="name")

    def __str__(self):
        return f"{self.title}, {self.status}, created by {self.created_by}"
    
    class Meta:
        verbose_name="task"
        verbose_name_plural = "tasks"