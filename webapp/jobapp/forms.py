from django import forms
from .models import PostJob


class PostJobForm(forms.ModelForm):
    class Meta:
        model = PostJob
        fields = ['positions', 'info_position', 'salary', 'diet']
