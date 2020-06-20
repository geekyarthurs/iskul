from django.contrib import admin
from .models import Admission
# Register your models here.


class admissionModel(admin.ModelAdmin):
    list_display = ('student_name', 'class_name','student_address','student_contact','date_of_admission', )

admin.site.register(Admission, admissionModel)
