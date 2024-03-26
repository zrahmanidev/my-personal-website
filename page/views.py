from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from resume.models import About
from django.views.generic.list import View
from .form import ContactUsForm
from slider.models import Slider
# from django_recaptcha.fields import ReCaptchaField
from django.views.generic import CreateView

from .models import ContactUs


def home(request):
    about = About.objects.first()
    slides = Slider.objects.all()
    context = {'about': about,
               'SEO_TITLE': 'home',
               'slides': slides
               }

    return render(request, 'home.html', context)



def about(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_page')
    else:
        form = ContactUsForm()
    return render(request, 'contact.html', {'form': form})


def contact_success_view(request):
    return render(request, 'contact.html')
# class Contact(View):
#     model = ContactUs
#     template_name = 'contact.html'
#     form = ContactUsForm()
#     context = {
#         'SEO_TITLE': 'contact',
#         'form': form
#     }

# def get(self, request):
#     return render(request, 'contact.html', {'form': form})
#
# def post(self, request):
#     request: HttpRequest = self.request
#     name = request.POST.get('name')
#     print(name)
#     # return render(request, 'contact.html', context)
#
#     form = ContactUsForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('contact')
# contact = ContactUs.objects.create()
# contact.name = request.POST.get('name')
# contact.email = request.POST.get('email')
# contact.subject = request.POST.get('subject')
# contact.message = request.POST.get('message')
# contact.save()
# else:
#     return render(request, 'contact.html', self.context)
