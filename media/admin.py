from django.contrib import admin
from .models import User
from .models import Content

# Register your models here.
admin.site.register(Content)
admin.site.register(User)