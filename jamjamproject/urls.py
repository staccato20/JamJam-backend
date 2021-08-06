"""jamjamproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import jamjamapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jamjamapp.views.layout, name='layout'),  # 임시메인
    path('detail/<str:id>/', jamjamapp.views.detail,
         name='detail'),  # 커뮤니티 게시글 자세히 보기
    path('community/<int:hashtag_id>/', jamjamapp.views.community,
         name='community'),  # 게시글 각 카테고리 페이지(해시태그로 치면 search)
    path('commu_write/create/', jamjamapp.views.create, name='create'),  # 게시글 C
    path('edit/<str:id>/', jamjamapp.views.edit, name='edit'),  # 게시글 수정
    path('delete/<str:id>/', jamjamapp.views.delete, name='delete'),  # 게시글 삭제
    path('delete_comment/<int:comment_id>/',
         jamjamapp.views.delete_comment, name='delete_comment'),  # 댓글 삭제
    path('like/<int:pk>', jamjamapp.views.like, name='like'),
    # ------민정이 개발-------

    path('', jamjamapp.views.layout, name='layout'),
    path('day_detail/', jamjamapp.views.day_detail, name='day_detail'),
    path('diary/diary_create', jamjamapp.views.diary_create, name='diary_create'),
    path('bucketlist_write/bucket_create', jamjamapp.views.bucket_create, name='bucket_create'),
    path('diary_detail/<str:id>/', jamjamapp.views.diary_detail, name='diary_detail'),
    path('diary_edit/<str:id>', jamjamapp.views.diary_edit, name='diary_edit'),
    path('p_edit/<str:id>', jamjamapp.views.p_edit, name='p_edit'),
    path('diary_delete/<str:id>/', jamjamapp.views.diary_delete, name='diary_delete'),
    path('profile/', jamjamapp.views.profile, name='profile'),
    path('bucketlist/', jamjamapp.views.bucketlist, name='bucketlist'),
    path('bucket_edit/<str:id>', jamjamapp.views.bucket_edit, name='bucket_edit'),
    path('bucket_delete/<str:id>/', jamjamapp.views.bucket_delete, name='bucket_delete'),
    path('bucket_detail/<str:id>/', jamjamapp.views.bucket_detail, name='bucket_detail'),
    # ------예찬이 개발-------
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
