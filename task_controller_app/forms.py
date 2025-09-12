from django.forms import ModelForm, CharField, ModelChoiceField, Form, ChoiceField
from task_controller_app.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 
            'description', 
            'due_date', 
            'task_type', 
            'task_priority', 
        ]
        
class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 
            'description', 
            'due_date', 
            'task_type', 
            'task_priority', 
        ]
        
class FilterForm(Form):
    task_type = ChoiceField(choices=Task.TYPE_CHOICES, required=False)
    task_priority = ChoiceField(choices=Task.PRIORITY_CHOICES, required=False)