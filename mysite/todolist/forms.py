from dataclasses import field
from socket import fromshare
from django import forms
from . models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name' , 'task_desc']
