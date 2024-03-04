from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='نام')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    subject = models.CharField(max_length=200, null=True, blank=True, verbose_name='موضوع')
    message = models.TextField(max_length=500, null=True, blank=True, verbose_name='پیام')

    class Meta:
        verbose_name = ' تماس با من'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.name
