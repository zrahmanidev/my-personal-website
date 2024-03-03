from django.shortcuts import render
from resume.models import About

from django.views.generic import CreateView


# from page import

# Create your views ()
# class home(CreateView):
#     template_name = 'page/home.html'
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(*a)
def home(request):
    about = About.objects.first()
    context = {'about': about}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
