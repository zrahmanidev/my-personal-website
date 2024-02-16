from django.shortcuts import render
from django.views.generic import DetailView, ListView
from resume.models import Resume, Skills


# Create your views here.

# class MyResume(DetailView):
#     pass
# def MyResume(request):
#     return render(request,'resume.html')

def my_resume(request):
    items = Resume.objects.all()
    skill_items = Skills.objects.all()
    context = {
        'items': items,
        'skills': skill_items

    }

    return render(request, 'resume.html', context)
