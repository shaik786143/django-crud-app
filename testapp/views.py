from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'testapp/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'testapp/task_form.html'
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'testapp/task_form.html'
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'testapp/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Task deleted successfully!')
        return super().delete(request, *args, **kwargs)
