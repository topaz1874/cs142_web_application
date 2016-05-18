from django.contrib import admin
from .models import User, Photo, Comments
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('file_name',)

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    fields = ('comment','photo', 'user')

    list_display = ('comment',)