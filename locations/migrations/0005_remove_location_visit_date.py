# Generated by Django 5.1.6 on 2025-03-02 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_alter_location_visit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='visit_date',
        ),
    ]
