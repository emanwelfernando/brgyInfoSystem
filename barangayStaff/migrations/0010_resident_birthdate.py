# Generated by Django 4.2.1 on 2023-05-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barangayStaff', '0009_alter_resident_gender_alter_resident_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='birthDate',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
