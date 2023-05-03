from django.db import models
from users.models import User
# Create your models here.


class TodoArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("할일 제목", max_length=50, null=True, blank=True)
    is_complete = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("생성 일시", auto_now_add=True)
    updated_at = models.DateTimeField("수정 일시", auto_now=True)
    completion_at = models.DateTimeField(
        "완료 날짜", null=True, default=None, blank=True)

    def __str__(self):
        return str(self.title)
