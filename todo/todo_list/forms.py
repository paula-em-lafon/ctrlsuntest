from .models import Task
from django import forms
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =["task_name",
                 "assigned_to",
                 "status",
                 "deadline",
        ]

        widgets = {
            'deadline': forms.DateInput(attrs={'min': timezone.localdate(), 'type':'date'}),
        }

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =["task_name",
                 "assigned_to",
                 "status",
                 "deadline",
        ]

        widgets = {
            'deadline': forms.DateInput( attrs={'type':'date'}),
        }

class AuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': gettext_lazy("Wrong Credentials"),
        'inactive': gettext_lazy("Wrong Credentials"),
    }

class RegisterForm(UserCreationForm):
    class Meta:
	    model = User
	    fields = ["username", "password1", "password2"]

class UserUpdateForm(UserCreationForm):
    class Meta:
	    model = User
	    fields = ["username", "password1", "password2"]