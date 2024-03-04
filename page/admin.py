from django.contrib import admin

from page.models import ContactUs
from resume.models import About


# Register your models here.
admin.site.register(About)
admin.site.register(ContactUs)