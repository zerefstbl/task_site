from django import forms
from .models import Tarefas


class RegisterTask(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = "__all__"
        context_object_name = 'tarefas'
