# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class Contents(models.Model):
    post_user = models.ForeignKey(AbstractUser.username,on_delete=models.CASCADE)
    post_id = models.IntegerField()
    create_time = models.DateTimeField('user created')
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.content

    # def was_published_recently(self):
    #     return self.create_time >= timezone.now() - datetime.timedelta(days=1)

