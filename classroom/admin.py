from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Chapter)

admin.site.register(models.Content)
admin.site.register(models.Grade)
admin.site.register(models.Subject)
