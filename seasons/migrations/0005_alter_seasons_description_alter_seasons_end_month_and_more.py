# Generated by Django 5.1.6 on 2025-03-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0004_rename_month_from_seasons_end_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasons',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='seasons',
            name='end_month',
            field=models.CharField(blank=True, choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], null=True),
        ),
        migrations.AlterField(
            model_name='seasons',
            name='start_month',
            field=models.CharField(blank=True, choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], null=True),
        ),
    ]
