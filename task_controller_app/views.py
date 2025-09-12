from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View 
from django.contrib.auth.mixins import LoginRequiredMixin 
from task_controller_app.models import Task 
from task_controller_app.forms import FilterForm, TaskForm, TaskUpdateForm 
from task_controller_app.mixins import CheckIsOwnerMixin
 
class TaskListView(CheckIsOwnerMixin, LoginRequiredMixin, ListView): 
    model = Task 
    template_name = 'task_controller_app/task_list.html' 
    context_object_name = 'tasks' 
    login_url = 'login_page' 
     
    def get_queryset(self): 
        queryset = super().get_queryset() 
         
        task_type = self.request.GET.get("task_type") 
        task_priority = self.request.GET.get("task_priority") 
         
        if task_type: 
            queryset = queryset.filter(task_type=task_type) 
             
        if task_priority: 
            queryset = queryset.filter(task_priority=task_priority) 
             
        return queryset 
     
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['form'] = FilterForm(self.request.GET) 
        return context 
     
class TaskDetailView(CheckIsOwnerMixin, LoginRequiredMixin, DetailView): 
    model = Task 
    template_name = 'task_controller_app/task_detail.html' 
    context_object_name = 'task' 
    login_url = 'login_page' 
 
class TaskCreateView(LoginRequiredMixin, CreateView): 
    model = Task 
    template_name = 'task_controller_app/task_form.html' 
    form_class = TaskForm 
    success_url = '/' 
    login_url = 'login_page' 
     
    def form_valid(self, form): 
        form.instance.created_by = self.request.user 
        return super().form_valid(form) 
     
class TaskDeleteView(CheckIsOwnerMixin, LoginRequiredMixin, DeleteView): 
    model = Task 
    template_name = 'task_controller_app/task_delete_form.html' 
    success_url = '/' 
    login_url = 'login_page' 
 
class TaskUpdateView(CheckIsOwnerMixin, LoginRequiredMixin, UpdateView): 
    model = Task 
    template_name = 'task_controller_app/task_update_form.html' 
    form_class = TaskUpdateForm 
    success_url = '/' 
    login_url = 'login_page' 
 
class TaskCompleteView(CheckIsOwnerMixin, LoginRequiredMixin, View): 
    login_url = 'login_page' 
     
    def get(self, request, *args, **kwargs): 
        task = self.get_task() 
        task.task_type = 3 
        task.save() 
        return redirect('task_list') 
     
    def get_task(self): 
        task_id = self.kwargs.get('pk') 
        return get_object_or_404(Task, pk=task_id)