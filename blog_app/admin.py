from django.contrib import admin

# Register your models here.
from blog_app import models
admin.site.register(models.Blog)
admin.site.register(models.Comment)
admin.site.register(models.Likes)
