from django.shortcuts import render
from announcement.models import Announcement

from django.db.models import Q

# Create your views here.
def announcement(request):
    if request.user.is_student:
            grade = request.user.student.grades

    else:
        
        grade = request.user.teacher.grades
        
    announcement = Announcement.objects.filter(
        Q(announcement_type="Public") | Q(class_name=grade)).order_by('-date_announced')[:10]
    context = {
        'announcements' : announcement,
    }
    print(announcement)
    return render(request , 'announcement/index.html', context)