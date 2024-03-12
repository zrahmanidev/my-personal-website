# Generated by Django 5.0.2 on 2024-03-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': ' تماس با من', 'verbose_name_plural': 'تماس با ما'},
        ),
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='ایمیل'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='موضوع'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='text',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='پیام'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام'),
        ),
    ]