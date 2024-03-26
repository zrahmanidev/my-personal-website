from django.db import models


# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to='image_slider', verbose_name='اسلایدها')
    target_url = models.CharField(max_length=50, verbose_name='لینک مقصد')
    caption = models.TextField(verbose_name='کپشن اسلاید')

    class TypeChoices(models.TextChoices):
        web = 'WB'
        app = 'AP'

    type = models.CharField(choices=TypeChoices,max_length=5, verbose_name='نوع اسلاید', null=True)

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.caption
