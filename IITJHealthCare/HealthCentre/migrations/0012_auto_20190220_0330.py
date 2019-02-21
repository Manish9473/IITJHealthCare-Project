# Generated by Django 2.1.5 on 2019-02-20 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCentre', '0011_doctor_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='prescriptionText',
            field=models.CharField(default='', max_length=2000),
        ),
    ]