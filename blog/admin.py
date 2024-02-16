from django.contrib import admin
from .models import Category, Post, PostComment
from . import models

# Register your models here.
# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  pass


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

# @admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Post)
admin.site.register(models.PostComment)
admin.site.register(models.Category)