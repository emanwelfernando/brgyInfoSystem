from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *

def dashboard(request):
    return render(request, 'barangayStaff/dashboard.html')

def household(request):
    return render(request, 'barangayStaff/household.html')

def resident(request):
    residents = Resident.objects.all()
    residentFilter = ResidentFilters(request.GET, queryset=residents)
    residents = residentFilter.qs
    context = {'residents': residents, 'residentFilter': residentFilter}
    return render(request, 'barangayStaff/resident.html', context)

def settings(request):
    return HttpResponse('Settings')

def logout(request):
    return HttpResponse('Logout')

def view_resident(request, pk):
    viewResidents = Resident.objects.get(id=pk)
    return render(request, 'barangayStaff/view_resident.html', {'viewResidents':viewResidents})

def createResident(request):
    form = residentForm()
    if request.method=="POST":
        form = residentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/resident')
    context = {'form':form}
    return render(request, 'barangayStaff/resident_form.html', context)

def updateResident(request, pk):
    resident = Resident.objects.get(id=pk)
    form = residentForm(instance = resident) 
    if request.method=="POST":
        form = residentForm(request.POST, instance=resident)
        if form.is_valid:
            form.save()
            return redirect('/resident')
    context = {'form':form}
    return render(request, 'barangayStaff/resident_form.html', context)

def deleteResident(request, pk):
    resident = Resident.objects.get(id=pk)
    if request.method=="POST":
        resident.delete()
        return redirect('/resident')
    context = {'resident':resident}
    return render(request, 'barangayStaff/delete_resident.html', context)

