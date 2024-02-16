from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    slug = models.SlugField(verbose_name='نامک')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    image = models.ImageField(upload_to='images', verbose_name='تصویر مقاله')
    short_description = models.TextField(null=True, blank=True, verbose_name='توضیحات کوتاه')
    body = models.TextField(null=True, blank=True, verbose_name='مطلب')
    slug = models.SlugField(verbose_name='نامک')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='دسته بندی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی')
    published_at = models.DateTimeField(null=True, verbose_name='تاریخ انتشار')

    class StatusChoices(models.TextChoices):
        PUBLISHED = "PS"
        DRAFT = "DR"
        REVIEW = "RE"

    status = models.CharField(
        max_length=2,
        choices=StatusChoices,
        default=StatusChoices.DRAFT,
    )

    def get_absolute_url(self):
        return "/blog/" + self.slug

    class Meta:
        verbose_name = 'نوشته'
        verbose_name_plural = 'نوشته ها'

    def __str__(self):
        return self.title


class PostComment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='کاربر')
    parent = models.ForeignKey('PostComment', on_delete=models.CASCADE, null=True, blank=True, verbose_name='والد')
    # related_name = 'reply'
    post_id = models.ForeignKey('Post', on_delete=models.PROTECT, verbose_name='پست')
    text = models.TextField(verbose_name='متن نظر')
    approved = models.BooleanField(default=False, verbose_name='قبول/رد')
    approved_by = models.CharField(max_length=50, null=True, verbose_name='پذیرنده نظر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد نظر')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی نظر')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return str(self.user_id)
