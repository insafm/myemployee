# Generated by Django 3.2.16 on 2022-11-03 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_salary', to='employee.employee'),
        ),
    ]