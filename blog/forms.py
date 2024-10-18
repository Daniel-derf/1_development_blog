from django import forms
from . import models as m

class PostForm(forms.ModelForm):
    class meta:
        model = m.Post
        fields= '__all__'
        exclude = ['created_at', 'updated_at']