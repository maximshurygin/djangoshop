# Generated by Django 4.2.4 on 2023-08-30 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]