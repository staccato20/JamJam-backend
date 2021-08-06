from django.db import models
from django.conf import settings

# 게시글


class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="likes")
    hits = models.PositiveIntegerField(default=0, verbose_name='views')

    def __str__(self):
        return self.Title

# 댓글


class Comment(models.Model):
    def __str__(self):
        return self.text

    post_id = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

# 커뮤니티 카테고리를 해시태그라고 편의상 해둠


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# ----민정이 개발 부분------


class Post(models.Model):
    diary_title = models.CharField(max_length=100)#제목
    diary_date = models.CharField(null = False, max_length=15, default='oooo년 oo월 oo일')#기록하고 싶은 날짜( ex) 여행 다녀온 날 등 )
    diary_body = models.TextField()#내용

    def __str__(self):
        return self.diary_title

#버킷리스트 모델
class Bucket(models.Model):
    bucket_title = models.CharField(max_length=100)#제목
    bucket_date = models.CharField(null = False, max_length=15, default='oooo년 oo월 oo일')#하고 싶은 날짜( ex) ~날 ~하기 등 )
    bucket_body = models.TextField()#내용

    def __str__(self):
        return self.bucket_title

#프로필 모델
class Profile(models.Model):
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname

# ----예찬이 개발 부분------
