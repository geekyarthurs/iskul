from django.contrib import admin
from django.contrib.auth.models import Group
from . import models
# Register your models here.

class subjectDetails(admin.ModelAdmin):
    list_display = ('class_name', 'course_name')


admin.site.register(models.Chapter)

admin.site.register(models.Content)
admin.site.register(models.Grade)
admin.site.register(models.Subject)
admin.site.unregister(Group)
