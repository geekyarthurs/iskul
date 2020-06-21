from django.contrib import admin
from .models import Announcement

# Register your models here.
class announceModel(admin.ModelAdmin):
    list_display = ('title', 'date_announced')



admin.site.register(Announcement, announceModel)