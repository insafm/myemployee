# Generated by Django 3.2.16 on 2022-11-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20221103_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
