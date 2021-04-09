from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.models import User
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm, AuthForm, RegisterForm, UserUpdateForm
from .filters import TaskFilter

class CustomLoginView(LoginView):
    template_name = "todo_list/login.html"
    authentication_form = AuthForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class RegisterView(LoginRequiredMixin, CreateView):
    template_name = "todo_list/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("tasks")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'todo_list/userupdate.html'
    success_url = reverse_lazy("tasks")
    redirect_authenticated_user = True
    
    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            update_session_auth_hash(self.request, user)
            return HttpResponseRedirect(reverse('tasks'))
        return super(UserUpdateView, self).form_valid(form)

    
class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy('login')
    def get_object(self, queryset=None):
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()  # deleting the default "User" model
        return HttpResponseRedirect(reverse('login'))


class TaskList(LoginRequiredMixin, FilterView):
    model = Task
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TaskCreate(LoginRequiredMixin, CreateView):
    template_name = "todo_list/task_form.html"
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks')

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todo_list/task.html"
    context_object_name = 'task'

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "todo_list/task_update.html"
    form_class = TaskUpdateForm
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "todo_list/task_confirm_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy('tasks')
    









