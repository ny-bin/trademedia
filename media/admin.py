from django.contrib import admin
from .models import User
from .models import Contents

# Register your models here.
admin.site.register(Contents)
admin.site.register(User)