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
    path('diary/create', jamjamapp.views.create, name='create'),
    path('detail/<str:id>/', jamjamapp.views.detail, name='detail'),
    path('edit/<str:id>', jamjamapp.views.edit, name='edit'),
    path('delete/<str:id>/', jamjamapp.views.delete, name='delete'),
    # ------예찬이 개발-------
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
