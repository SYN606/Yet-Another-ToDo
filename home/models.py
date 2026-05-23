from django.contrib.auth.models import AbstractUser
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class CustomUser(AbstractUser):
    full_name = models.CharField(
        max_length=150,
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Todo(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="todos",
    )
    title = models.CharField(max_length=200, )
    description = CKEditor5Field(
        "Description",
        config_name="extends",
        blank=True,
        null=True,
    )
    completed = models.BooleanField(default=False, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return f"{self.title} ({self.user.username})"
