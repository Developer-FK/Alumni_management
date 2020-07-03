from django import forms
from .models import BlogPost, Files_Of_posts, Comment







class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','body']


class BlogPostWithFilesForm(BlogPostForm):

    files = forms.FileField(required = False, widget = forms.ClearableFileInput(attrs = {'multiple' : True}))
    fields = BlogPostForm.Meta.fields + ['files',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]