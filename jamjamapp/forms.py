from django import forms
from .models import Blog, Comment, Hashtag, Post  # 민정


class CreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['Title', 'Content', 'Image', 'hashtags']  # 카톡완료 후 작성자 추가하기


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

# ----민정이 개발 부분------


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'date', 'body']  # 제목, 날짜, 내용

# ----예찬이 개발 부분------
