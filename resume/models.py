from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class About(models.Model):
    first_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='نام خانوادگی')
    nick_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='نام مستعار')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='آدرس')
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='موبایل')
    web = models.CharField(max_length=200, null=True, blank=True, verbose_name='سایت')
    Entertainment = models.CharField(max_length=300, null=True, blank=True, verbose_name='سرگرمی')
    fax = models.CharField(max_length=300, null=True, blank=True, verbose_name='فکس')
    birthday = models.CharField(max_length=300, null=True, blank=True, verbose_name='تاریخ تولد')
    employ = models.CharField(max_length=300, null=True, blank=True, verbose_name='وضعیت استخدام')

    class Meta:
        verbose_name = ' درباره'
        verbose_name_plural = 'درباره'

    def __str__(self):
        return self.nick_name


class Resume(models.Model):
    title = models.CharField(max_length=100, verbose_name='محل')
    subtitle = models.CharField(max_length=100, verbose_name='سمت')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    from_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ شروع')
    to_date = models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ انتها')
    priority = models.IntegerField(verbose_name='اولویت')
    status_chioce = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    # status = models.CharField
    # type=

    class Typechoice(models.TextChoices):
        EDUCATION = "ED"
        WORK = "WO"
        HONORS = "HO"

    type = models.CharField(max_length=50, choices=Typechoice, default=Typechoice.EDUCATION, verbose_name='نوع')

    class Meta:
        verbose_name = 'رزومه من'
        verbose_name_plural = 'رزومه های من'

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=100, verbose_name=' عنوان')
    lables = models.CharField(max_length=100, verbose_name='برچسب')
    percent = models.IntegerField(default=1,
                                  validators=[MinValueValidator(1), MaxValueValidator(100)]
                                  )

    class Typechoice(models.TextChoices):
        DESIGN = "DE"
        PROGRAMMING = "PR"

    type = models.CharField(max_length=50, choices=Typechoice, default=Typechoice.DESIGN, verbose_name='نوع')

    class Meta:
        verbose_name = 'مهارت من'
        verbose_name_plural = 'مهارت های من'

    def __str__(self):
        return self.title
