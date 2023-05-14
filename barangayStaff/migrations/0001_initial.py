# Generated by Django 4.2.1 on 2023-05-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('age', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('undecided', 'undecided')], max_length=50, null=True)),
                ('status', models.CharField(choices=[('single', 'single'), ('married', 'married')], max_length=50, null=True)),
            ],
        ),
    ]
