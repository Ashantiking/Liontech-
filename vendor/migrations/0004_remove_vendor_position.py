# Generated by Django 3.2.9 on 2021-11-21 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_remove_vendor_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='position',
        ),
    ]
