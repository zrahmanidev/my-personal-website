from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from resume.models import About
from django.views.generic.list import View
from django.views.generic import CreateView

from .models import ContactUs


# from page import

# Create your views ()
# class home(CreateView):
#     template_name = 'page/home.html'
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(*a)
def home(request):
    about = About.objects.first()
    context = {'about': about,
               'SEO_TITLE': 'home'}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


class Contact(View):
    model = ContactUs
    template_name = 'contact.html'
    context = {
        'SEO_TITLE': 'contact'
    }

    def get(self, request):
        return render(request, 'contact.html', )

    def post(self, request):
        request: HttpRequest = self.request
        name = request.POST.get('name')
        print(name)
        # return render(request, 'contact.html', context)
        contact = ContactUs.objects.create()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()

        return render(request, 'contact.html', self.context)
