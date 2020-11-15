# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from loginauth.models import User
# from django.contrib.auth.models import User



class Content(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(
        upload_to="../images/images", blank=True, null=True)
    content = models.TextField(blank=False)
    title = models.CharField(max_length=20,blank=False)
    published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.content

    # def was_published_recently(self):
    #     return self.create_time >= timezone.now() - datetime.timedelta(days=1)

