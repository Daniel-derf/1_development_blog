from django import forms
from . import models as m

class PostForm(forms.ModelForm):
    class Meta:
        model = m.Post
        fields= '__all__'
        exclude = ['created_at', 'updated_at']