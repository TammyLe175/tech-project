from django import forms
from .models import App

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['id', 'task', 'task_description','name', 'status']
        # css applying
        widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task name',
            }),
            'task_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the task',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter your name",
            }),
            'status': forms.RadioSelect(choices=App.status_options)

        }