from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'previewText', 'content', 'previewImage', ]

        # widgets = {
        #     'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        # }
