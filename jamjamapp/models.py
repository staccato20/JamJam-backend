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
    title = models.CharField(max_length=100)  # 제목
    write_date = models.DateField('date published')  # 쓴 날짜
    # 기록하고 싶은 날짜( ex) 여행 다녀온 날 등 )
    date = models.CharField(null=False, max_length=15, default='oooo년 oo월 oo일')
    body = models.TextField()  # 내용

    def __str__(self):
        return self.title

# ----예찬이 개발 부분------
