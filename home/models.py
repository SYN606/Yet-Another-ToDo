from django.db import models
from django.contrib.auth.models import User
# from django_ckeditor_5.fields import CKEditor5Field


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
