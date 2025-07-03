from django.db import models
from django.contrib.auth.models import AbstractUser
from django_ckeditor_5.fields import CKEditor5Field


class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    """
    full_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Todo(models.Model):
    """
    ToDo model to store user tasks.
    """
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             related_name='todos')
    title = models.CharField(max_length=200)
    description = CKEditor5Field(
        'Text', config_name='extends')  # rich text editor here
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "ToDo"
        verbose_name_plural = "ToDos"
