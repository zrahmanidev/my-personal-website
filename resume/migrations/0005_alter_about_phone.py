# Generated by Django 5.0.2 on 2024-03-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_about_options_about_entertainment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.CharField(blank='-', max_length=100, null=True, verbose_name='موبایل'),
        ),
    ]