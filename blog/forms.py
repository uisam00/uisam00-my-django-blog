from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=250)
    article = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'article', 'category', 'image', 'status',)
