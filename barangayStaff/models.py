from django.db import models


GENDER = (
    ('male', 'male'),
    ('female', 'female'),
    ('undecided', 'undecided'),
)
STATUS = (
    ('single', 'single'),
    ('married', 'married'),
)

class Resident(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    age = models.IntegerField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True, choices=GENDER)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return self.name

class Household(models.Model):
    name = models.CharField(max_length=50, null=True)
    householdSize = models.IntegerField(null=True)
    houseHoldHead = models.ForeignKey(Resident, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name