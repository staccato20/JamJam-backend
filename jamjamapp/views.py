from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, Comment, Hashtag, Post, Profile, Bucket
from .forms import CreateForm, CommentForm, PostForm, ProfileForm, BucketForm
from datetime import date, datetime, timedelta

# Create your views here.


def layout1(request):
    return render(request, 'layout1.html')


def layout2(request):
    return render(request, 'layout2.html')


def login(request):
    return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')
# ------frontend 개발-------

# 임시 메인페이지
def layout(request):
    blogs = Blog.objects
    hashtag = Hashtag.objects
    return render(request, 'layout(M).html', {'blogs': blogs, 'hashtag': hashtag})

# 커뮤니티 첫 페이지
def community(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    blogs = Blog.objects
    return render(request, 'community/community.html', {'blogs': blogs, 'hashtag': hashtag})

# 커뮤니티 Write
def commu_write(request):
    return render(request, 'community/commu_write.html')

# 커뮤니티
def create(request, blog=None):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.Write_day = timezone.datetime.now()
            blog.save()
            form.save_m2m()
            return redirect('layout')
    else:
        form = CreateForm(instance=blog)
        return render(request, 'community/commu_write.html', {'form': form})

# 커뮤니티 게시글 자세히 보기 페이지


def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail', id)
    else:
        form = CommentForm()
        return render(request, 'community/detail.html', {'blog': blog, 'form': form})

# 커뮤니티

def edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('detail', id)
    else:
        form = CreateForm(instance=blog)
    return render(request, 'community/edit.html', {'form': form})

# 게시글 삭제


def delete(request, id):
    delete_blog = get_object_or_404(Blog, id=id)
    delete_blog.delete()
    return redirect('layout')

# 댓글 삭제


def delete_comment(request, comment_id):
    delete_comment = get_object_or_404(Comment, id=comment_id)
    delete_comment.delete()
    return redirect('detail', comment_id)

# 좋아요


def like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    blog = get_object_or_404(Blog, pk=pk)
    user = request.user

    if blog.likes.filter(id=user.id).exists():
        blog.likes.remove(user)
    else:
        blog.likes.add(user)

    return redirect('detail', pk)
# ------민정이 개발-------

def layout_Y(request):
    return render(request, 'layout(Y).html')

def day_detail(request):
    posts = Post.objects
    return render(request, 'day_detail.html', {'posts':posts})

def profile(request):
    profiles = Profile.objects
    return render(request, 'mypage/profile.html', {'profiles':profiles})

def bucketlist(request):
    buckets = Bucket.objects
    return render(request, 'bucketlist.html', {'buckets':buckets})

#다이어리 작성
def diary_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('layout_Y')
    else:
        form = PostForm
        return render(request, 'diary.html', {'form':form})

#버킷리스트 작성
def bucket_create(request):
    if request.method == "POST":
        form = BucketForm(request.POST)
        if form.is_valid():
            bucket = form.save(commit=False)
            bucket.save()
            return redirect('layout_Y')
    else:
        form = BucketForm
        return render(request, 'bucketlist_write.html', {'form':form})

#다이어리 디테일
def diary_detail(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_id = post
            post.text = form.cleaned_data['text']
            post.save()
            return redirect('day_detail_write', id)
    else:
        form=PostForm()
        return render(request, 'day_detail_detail.html', {'post':post, 'form':form})

#버킷리스트 디테일
def bucket_detail(request, id):
    bucket = get_object_or_404(Bucket, id = id)
    if request.method == 'POST':
        form = BucketForm(request.POST)
        if form.is_valid():
            bucket = form.save(commit=False)
            bucket.post_id = bucket
            bucket.text = form.cleaned_data['text']
            bucket.save()
            return redirect('layout_Y', id)
    else:
        form=BucketForm()
        return render(request, 'bucketlist_detail.html', {'bucket':bucket, 'form':form})

#데이디테일 수정
def diary_edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('layout_Y')
    else:
        form = PostForm(instance=post)
        return render(request, 'diary_edit.html', {'form':form})

#버킷리스트 수정
def bucket_edit(request, id):
    bucket = get_object_or_404(Bucket, id = id)
    if request.method == "POST":
        form = BucketForm(request.POST, instance=bucket)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('layout_Y')
    else:
        form = BucketForm(instance=bucket)
        return render(request, 'bucketlist_edit.html', {'form':form})

#프로필 (비번)수정
def p_edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('layout_Y')
    else:
        form = ProfileForm(instance=post)
        return render(request, 'profile_edit.html', {'form':form})

#다이어리 삭제
def diary_delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('layout_Y')

#버킷리스트 삭제
def bucket_delete(request, id):
    delete_bucket = get_object_or_404(Bucket, id = id)
    delete_bucket.delete()
    return redirect('layout_Y')

#젬 결제
# def pay(request):
#     if request.method == "POST":
#         URL = 'https://kapi.kakao.com/v1/payment/ready'
#         headers = {
#             "Authorization": "KakaoAK " + "Kakao Developers에서 생성한 앱의 어드민 키",   # 변경불가
#             "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
#         }
#         params = {
#             "cid": "TC0ONETIME",    # 테스트용 코드
#             "partner_order_id": "1001",     # 주문번호
#             "partner_user_id": "german",    # 유저 아이디
#             "item_name": "연어초밥",        # 구매 물품 이름
#             "quantity": "1",                # 구매 물품 수량
#             "total_amount": "12000",        # 구매 물품 가격
#             "tax_free_amount": "0",         # 구매 물품 비과세
#             "approval_url": "결제 성공 시 이동할 url",
#             "cancel_url": "결제 취소 시 이동할 url",
#             "fail_url": "결제 실패 시 이동할 url",
#         }

#         res = requests.post(URL, headers=headers, params=params)
#         request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
#         next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
#         return redirect(next_url)


#     return render(request, 'shop/pay.html')
# ------예찬이 개발-------
