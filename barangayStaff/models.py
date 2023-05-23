from django.db import models
from django import forms
from datetime import datetime, date

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Undecided', 'Undecided'),
)
STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
)
VACCINATION = (
    ('Vaccinated', 'Vaccinated'),
    ('Not Vaccinated', 'Not Vaccinated'),
)

class Resident(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)        
    birth_date = models.DateField(null=True)
    age = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True, choices=GENDER)
    vaccination = models.CharField(max_length=50, null=True, choices=VACCINATION)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return self.name

class Household(models.Model):
    name = models.CharField(max_length=50, null=True)
    householdSize = models.IntegerField(null=True)
    houseHoldHead = models.ForeignKey(Resident, null=True, on_delete=models.SET_NULL)
   

    def __str__(self):
        return self.name