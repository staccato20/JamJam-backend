from django import forms
from .models import Blog, Comment, Hashtag, Post, Profile, Bucket


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
        fields = ['diary_title', 'diary_date', 'diary_body']#제목, 날짜, 내용

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname']

class BucketForm(forms.ModelForm):
    class Meta:
        model = Bucket
        fields = ['bucket_title', 'bucket_date', 'bucket_body']#제목, 날짜, 내용

# ----예찬이 개발 부분------
