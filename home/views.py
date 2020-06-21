from django.shortcuts import render
from classroom.models import  Subject
from accounts.models import Student, Teacher 
# Create your views here.
def home(request):
    studentCount = Student.objects.all().count()
    subjectCount = Subject.objects.all().count()
    teacherCount = Teacher.objects.all().count()

    context = {
        'studentCount' : studentCount,
        'subjectCount' : subjectCount,
        'teacherCount' : teacherCount,
    }

    return render(request, 'index.html', context)
