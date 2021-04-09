from django import forms
from .models import Post
# from .models import Language
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)