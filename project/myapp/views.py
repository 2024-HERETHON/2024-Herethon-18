from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from myapp.forms import CommentForm
from .models import BoardPost, Friendship, Reflection
from django.views.decorators.http import require_POST
import json
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import TruncDate
from django.db.models.functions import TruncDay
from django.db.models import Count
from .models import Comment, Reflection
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import Comment
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import logging


def main(request):
    context = {}

    if request.user.is_authenticated:
        try:
            kakao_user = KakaoUser.objects.get(user=request.user)
            context["username"] = kakao_user.nickname
        except KakaoUser.DoesNotExist:
            try:
                naver_user = NaverUser.objects.get(user=request.user)
                context["username"] = naver_user.nickname
            except NaverUser.DoesNotExist:
                # 로그인은 되어 있으나, 어느 쪽 데이터베이스에도 사용자 정보가 없는 경우
                context["username"] = None
    else:
        # 사용자가 로그인하지 않은 경우
        context["username"] = None

    recent_posts = BoardPost.objects.order_by("-created_at")[:15]
    most_viewed_posts = BoardPost.objects.order_by("-likes")[:15]
    popular_posts = BoardPost.objects.order_by("-likes")[:15]

    context.update(
        {
            "recent_posts": recent_posts,
            "most_viewed_posts": most_viewed_posts,
            "popular_posts": popular_posts,
        }
    )

    return render(request, "main.html", context)


def board_list(request):
    return render(request, "board_list.html")


from django.contrib.auth.decorators import login_required
from .models import BoardPost
from .models import KakaoUser, NaverUser


def board_create(request):
    return render(request, "board_create.html")


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "login_create.html"


def grow_1(request):
    return render(request, "grow_1.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        user_id = request.POST["id"]
        password = request.POST["password"]
        email = request.POST["email"]

        if User.objects.filter(username=user_id).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        user = User.objects.create_user(
            username=user_id, password=password, email=email
        )
        user.save()

        user = authenticate(username=user_id, password=password)
        login(request, user)

        return redirect("login")

    return render(request, "signup.html")


@login_required
def grow_3(request, reflection_id):
    reflection = get_object_or_404(Reflection, id=reflection_id, user=request.user)
    return render(request, "grow_3.html", {"reflection": reflection})


def mypage_share(request):
    return render(request, "mypage_share.html")


@login_required
def board_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        development_period = request.POST.get("development_period")
        participants = request.POST.get("participants")
        language = request.POST.get("language")
        file = request.FILES.get("file")

        BoardPost.objects.create(
            title=title,
            content=content,
            development_period=development_period,
            participants=participants,
            language=language,
            file=file,
            user=request.user,
        )
        return redirect("board_list")
    return render(request, "board_create.html")


@login_required
@require_POST
def like_post(request, post_id):
    data = json.loads(request.body.decode("utf-8"))
    post = get_object_or_404(BoardPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({"likes": post.likes.count(), "liked": liked})


@login_required
@require_POST
def dislike_post(request, post_id):  # Ensure post_id is accepted as an argument
    data = json.loads(request.body.decode("utf-8"))
    post = get_object_or_404(BoardPost, id=post_id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
        disliked = False
    else:
        post.dislikes.add(request.user)
        disliked = True
    return JsonResponse({"dislikes": post.dislikes.count(), "disliked": disliked})


@login_required
def board_list(request):
    # 게시물 목록을 가져오는 로직
    return render(request, "board_list.html")


@login_required
def grow_1(request):
    user_posts = BoardPost.objects.filter(user=request.user)
    total_likes = sum(post.likes.count() for post in user_posts)
    total_posts = user_posts.count()

    # 날짜별 좋아요 수 집계
    likes_data = (
        BoardPost.objects.filter(user=request.user)
        .annotate(date=TruncDay("created_at"))
        .values("date")
        .annotate(likes_count=Count("likes"))
        .order_by("date")
    )

    dates = [data["date"].strftime("%Y-%m-%d") for data in likes_data]
    like_counts = [data["likes_count"] for data in likes_data]

    context = {
        "total_likes": total_likes,
        "total_posts": total_posts,
        "user_posts": user_posts,
        "dates": dates,
        "like_counts": like_counts,
    }
    return render(request, "grow_1.html", context)


# @login_required
# def board_detail(request, post_id):
#     post = get_object_or_404(BoardPost, id=post_id)


#     context = {
#         "post": post,
#     }
#     return render(request, "board_detail.html", context)


def map_period(input):
    if input <= 3:
        return "0-3"
    elif input <= 7:
        return "4-7"
    elif input <= 11:
        return "8-11"
    else:
        return "12+"


def map_participants(input):
    if input <= 6:
        return "1-6"
    elif input <= 12:
        return "7-12"
    elif input <= 18:
        return "13-18"
    else:
        return "19+"


def search_view(request):
    search_query = request.GET.get("q", "")  # 'q'는 검색창에서 입력한 쿼리를 받습니다.
    search_criteria = request.GET.get("criteria", "title")

    # 선택한 기준에 따라 BoardPost 객체 필터링
    if search_criteria == "title":
        results = BoardPost.objects.filter(title__icontains=search_query)
    elif search_criteria == "content":
        results = BoardPost.objects.filter(content__icontains=search_query)
    elif search_criteria == "language":
        results = BoardPost.objects.filter(language__icontains=search_query)
    elif search_criteria == "development_period":
        mapped_period = map_period(int(search_query))
        results = BoardPost.objects.filter(development_period=mapped_period)
    elif search_criteria == "participants":
        mapped_participants = map_participants(int(search_query))
        results = BoardPost.objects.filter(participants=mapped_participants)
    else:
        results = BoardPost.objects.none()

    return render(
        request, "home_search.html", {"results": results, "query": search_query}
    )


def board_list(request):
    posts = BoardPost.objects.all()  # 데이터베이스에서 모든 게시물을 가져옴
    return render(request, "board_list.html", {"posts": posts})


def mypage_setting(request):
    return render(request, "mypage_setting.html")


def update(request, post_id):
    if request.method == "POST":
        post = BoardPost.objects.get(
            pk=post_id
        )  # 예시로 사용할 모델에 맞게 수정해야 합니다.

        # 새로운 데이터 저장
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.participants = request.POST.get("participants")
        post.development_period = request.POST.get("development_period")
        post.language = request.POST.get("language")
        post.updated_at = timezone.now()

        # 파일 업로드 처리 (필요시)
        if "file" in request.FILES:
            file = request.FILES["file"]
            # 파일 처리 로직 추가

        new_language = request.POST.get("language")
        if new_language:
            post.language = new_language

        # 저장
        post.save()
        return redirect("/detail/" + str(post.id))

    # GET 요청 처리 (옵션)
    else:
        post = BoardPost.objects.get(pk=post_id)
        context = {"post": post}
        return render(request, "board_update.html", context)


def delete(request, post_id):
    post = BoardPost.objects.get(id=post_id)
    post.delete()
    return redirect("main")


@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        boardpost = get_object_or_404(BoardPost, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.boardpost = boardpost
            comment.user = request.user
            comment.save()
        return redirect("board_detail", pk=boardpost.pk)
    return redirect("login")


@require_POST
def comment_delete(request, boardpost_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect("board_detail", pk=boardpost_pk)


def logout_view(request):
    logout(request)
    return redirect("main")  # 로그아웃 후 리디렉션 될 페이지


@login_required
def after_login(request):
    return render(request, "after_login.html", {"username": request.user.username})


@login_required
def board_detail(request, post_id):
    post = get_object_or_404(BoardPost, pk=post_id)
    comments = Comment.objects.filter(post=post)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("board_detail", post_id=post.id)

    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        "boardpost": post,
    }
    return render(request, "board_detail.html", context)


def grow_2(request, post_id):
    post = get_object_or_404(BoardPost, pk=post_id)
    context = {
        "post": post,
    }
    return render(request, "grow_2.html", context)


@login_required
def save_reflection(request, post_id):
    post = get_object_or_404(BoardPost, pk=post_id)
    if request.method == "POST":
        content = request.POST.get("reflection_content")
        if content:
            reflection = Reflection.objects.create(
                user=request.user, post=post, content=content
            )
            reflection.save()
            # 이 부분에서 reflection.id를 URL에 포함시켜야 합니다.
            return redirect("grow_3", reflection_id=reflection.id)
    return render(request, "grow_2.html", {"post": post})


@login_required
def view_reflection(request, reflection_id):
    reflections = Reflection.objects.filter(user=request.user)
    return render(request, "view_reflection.html", {"reflection": reflection})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            messages.error(request, "회원정보가 없습니다!")
    return render(request, "login.html", {"form": AuthenticationForm()})


@login_required
def edit_reflection(request, reflection_id):
    reflection = get_object_or_404(Reflection, pk=reflection_id, user=request.user)
    if request.method == "POST":
        form = ReflectionForm(request.POST, instance=reflection)
        if form.is_valid():
            form.save()
            return redirect("grow_3")
    else:
        form = ReflectionForm(instance=reflection)
    return render(request, "edit_reflection.html", {"form": form})


@login_required
def delete_reflection(request, reflection_id):
    reflection = get_object_or_404(Reflection, pk=reflection_id, user=request.user)
    if request.method == "POST":
        reflection.delete()
        return redirect(
            "some_view_name"
        )  # Redirect to a confirmation page or the main page
    return render(request, "confirm_delete.html", {"reflection": reflection})


logger = logging.getLogger(__name__)


@login_required
@require_POST
def check_email(request):
    data = json.loads(request.body)
    email = data.get("email")
    users = User.objects.filter(email=email)
    if users.exists():
        return JsonResponse(
            {"status": "success", "message": "이메일이 확인되었습니다."}
        )
    else:
        return JsonResponse({"status": "fail", "message": "해당 사용자가 없습니다!"})


@login_required
@require_POST
def add_friend(request):
    data = json.loads(request.body)
    email = data.get("email")
    users = User.objects.filter(email=email)
    if users.exists():
        friend = users.first()  # Take the first user if multiple exist
        if friend != request.user:  # Prevent adding self as friend
            Friendship.objects.get_or_create(creator=request.user, friend=friend)
            return JsonResponse(
                {"status": "success", "message": "친구로 추가되었습니다!"}
            )
        else:
            return JsonResponse(
                {"status": "fail", "message": "자기 자신을 친구로 추가할 수 없습니다."}
            )
    else:
        return JsonResponse({"status": "fail", "message": "해당 사용자가 없습니다!"})


from django.db.models import Count


def grow_1_view(request):
    user_posts = BoardPost.objects.filter(user=request.user)
    reflections = Reflection.objects.filter(user=request.user)

    print("Reflections Count:", reflections.count())  # 서버 로그에 반영 개수 출력

    return render(
        request,
        "grow_1.html",
        {
            "user_posts": user_posts,
            "reflections": reflections,
            "total_posts": user_posts.count(),
            "total_likes": sum(post.likes.count() for post in user_posts),
        },
    )
