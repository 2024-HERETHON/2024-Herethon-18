from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class KakaoUser(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=10, blank=True)
    age_range = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nickname


class NaverUser(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=10, blank=True)
    age_range = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nickname


class BoardPost(models.Model):
    DEVELOPMENT_PERIOD_CHOICES = [
        ("0-3", "0~3개월"),
        ("4-7", "4~7개월"),
        ("8-11", "8~11개월"),
        ("12+", "12개월 이상"),
    ]

    PARTICIPANTS_CHOICES = [
        ("1-6", "1~6명"),
        ("7-12", "7~12명"),
        ("13-18", "13~18명"),
        ("19+", "19명 이상"),
    ]

    LANGUAGE_CHOICES = [
        ("python", "Python"),
        ("numpy", "Numpy"),
        ("pandas", "Pandas"),
        ("java", "Java"),
        ("javascript", "JavaScript"),
        ("django", "Django"),
        ("html", "HTML"),
        ("css", "CSS"),
        ("c++", "C++"),
        ("other", "직접입력"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    development_period = models.CharField(
        max_length=5, choices=DEVELOPMENT_PERIOD_CHOICES
    )
    participants = models.CharField(max_length=6, choices=PARTICIPANTS_CHOICES)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    file = models.ImageField(upload_to="uploads/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    dislikes = models.ManyToManyField(User, related_name="disliked_posts", blank=True)
    reflection_num = models.BooleanField(default=False)

    def __str__(self):
        return self.title


from django.db import models
from django.conf import settings


class Comment(models.Model):
    post = models.ForeignKey(
        "BoardPost", on_delete=models.CASCADE, related_name="comments", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # 댓글의 처음 20자만 표시


class Reflection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BoardPost, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # 회고록이 작성되었으므로 해당 게시물의 reflection 필드를 True로 설정
        self.post.reflection_num = True
        self.post.save()

    def __str__(self):
        return self.content[:50]


class Friendship(models.Model):
    creator = models.ForeignKey(
        User, related_name="friendship_creator_set", on_delete=models.CASCADE
    )
    friend = models.ForeignKey(
        User, related_name="friend_set", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.creator.username} is friends with {self.friend.username}"
