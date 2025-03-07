# Generated by Django 5.1.7 on 2025-03-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Spring', 'Spring 🌸'), ('Summer', 'Summer ☀️'), ('Autumn', 'Autumn 🍂'), ('Winter', 'Winter ❄️')])),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('start_month', models.CharField(blank=True, choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], null=True)),
                ('end_month', models.CharField(blank=True, choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], null=True)),
            ],
        ),
    ]
