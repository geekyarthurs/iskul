from django.contrib import admin
from django.contrib.auth.models import Group
from . import models
# Register your models here.

class contentDetails(admin.ModelAdmin):
    list_display = ('topic', 'course_name', 'uploaded_at', 'uploaded_by')


admin.site.register(models.Chapter)
admin.site.register(models.Content ,contentDetails)
admin.site.register(models.Grade)
admin.site.register(models.Subject)

