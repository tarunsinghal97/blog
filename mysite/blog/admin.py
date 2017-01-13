from django.contrib import admin
from .models import blog, User
# Register your models here.
admin.site.register(blog)
admin.site.register(User)