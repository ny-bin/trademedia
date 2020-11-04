# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
# class CustomUser(AbstractUser):
#     pass

class Contents(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(
        upload_to="image/posts/", blank=True, null=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.content

    # def was_published_recently(self):
    #     return self.create_time >= timezone.now() - datetime.timedelta(days=1)

