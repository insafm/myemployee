# Generated by Django 3.2.16 on 2022-11-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male')], max_length=1),
        ),
    ]
