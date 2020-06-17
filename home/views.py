from django.shortcuts import render
from classroom.models import Grade, Subject, Content, Chapter

# Create your views here.
def home(request):
    gradeCount = Grade.objects.all().count()
    subjectCount = Subject.objects.all().count()
    contentCount = Content.objects.all().count()
    chapterCount = Chapter.objects.all().count()
    context = {
        'gradeCount' : gradeCount,
        'subjectCount' : subjectCount,
        'contentCount' : contentCount,
        'chapterCount' :chapterCount
    }
    return render(request, 'index.html', context)

