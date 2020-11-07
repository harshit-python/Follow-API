from django.contrib import admin
from . models import User
from .models import Following

admin.site.register(User)
admin.site.register(Following)

