# Generated by Django 5.0.2 on 2024-03-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_alter_skills_lables_alter_skills_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': ' درباره', 'verbose_name_plural': 'درباره'},
        ),
        migrations.AddField(
            model_name='about',
            name='Entertainment',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='سرگرمی'),
        ),
        migrations.AddField(
            model_name='about',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='آدرس'),
        ),
        migrations.AddField(
            model_name='about',
            name='birthday',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='ایمیل'),
        ),
        migrations.AddField(
            model_name='about',
            name='employ',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='وضعیت استخدام'),
        ),
        migrations.AddField(
            model_name='about',
            name='fax',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='فکس'),
        ),
        migrations.AddField(
            model_name='about',
            name='first_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='نام'),
        ),
        migrations.AddField(
            model_name='about',
            name='last_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='نام خانوادگی'),
        ),
        migrations.AddField(
            model_name='about',
            name='nick_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='نام مستعار'),
        ),
        migrations.AddField(
            model_name='about',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='موبایل'),
        ),
        migrations.AddField(
            model_name='about',
            name='web',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='سایت'),
        ),
    ]
