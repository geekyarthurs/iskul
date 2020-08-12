from django.shortcuts import render
from .models import Content , file
from django.core.paginator import Paginator

# Create your views here.
def contentDetails(request, slug):
    
    contents = Content.objects.all()
    content = Content.objects.get(slug=slug)
    files = file.objects.filter(content=content.id)
    context = {
        'content':content,
        'contents':contents,
        'files':files,
    }

    return render(request, 'contents/content.html', context)

def contents(request):
    content_list = Content.objects.all()
    page = request.GET.get('page', 1)    
    paginator = Paginator(content_list, 5)
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)


    return render(request, 'contents/allcontent.html', {'contents':contents})