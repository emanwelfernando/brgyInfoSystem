# Generated by Django 4.2.1 on 2023-05-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barangayStaff', '0007_alter_resident_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='vaccination',
            field=models.CharField(choices=[('vaccinated', 'vaccinated'), ('not vaccinated', 'not vaccinated')], max_length=50, null=True),
        ),
    ]