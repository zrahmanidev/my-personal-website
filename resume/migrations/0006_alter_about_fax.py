# Generated by Django 5.0.2 on 2024-03-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_alter_about_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='fax',
            field=models.CharField(blank='-', max_length=300, null=True, verbose_name='فکس'),
        ),
    ]