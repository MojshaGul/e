from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Task(models.Model):
    TYPE_CHOICES = [
        (1, "To Do"),
        (2, "In Progress"),
        (3, "Completed"),
        (4, "On Hold"),
        (5, "Cancelled")
    ]
    
    PRIORITY_CHOICES = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High")
    ]
    
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    due_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    
    task_type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    task_priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title