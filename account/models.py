# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
#
# # Create your models here.
# class User(AbstractUser):
#     mobile=models.CharField(max_length=100, verbose_name='تلفن همراه')
#     email_active_code=models.CharField(max_length=100,verbose_name='ایمیل')
#     about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
#     avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر پروفایل')
#
#     class Meta:
#         verbose_name = 'کاربر'
#         verbose_name_plural = 'کاربران'
#
#     def __str__(self):
#         if self.first_name is not '' and self.last_name is not '':
#             return self.get_full_name()
