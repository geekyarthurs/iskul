from django.shortcuts import render
from announcement.models import Announcement
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def announcement(request):
    if request.user.is_student:
            grade = request.user.student.grades

    else:
        
        grade = request.user.teacher.grades

    announcement_list = Announcement.objects.filter(
        Q(announcement_type="Public") | Q(class_name=grade)).order_by('-date_announced')


    page = request.GET.get('page', 1)    
    paginator = Paginator(announcement_list, 3)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)


    context = {
        'announcements' : announcements,
    }
    print(announcement)
    return render(request , 'announcement/index.html', context)