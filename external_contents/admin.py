from django.contrib import admin
from .models import Category , Content , file
# Register your models here.

class FileTabularInline(admin.TabularInline):
    model = file
    class Meta:
        model = Content
    

class ContentAdmin(admin.ModelAdmin):
    inlines = [FileTabularInline]
    list_display =['name', 'posted_on']

admin.site.register(Content, ContentAdmin)

class category(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, category)