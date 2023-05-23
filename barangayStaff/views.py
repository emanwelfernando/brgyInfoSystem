from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator

def dashboard(request):
    total_residents = Resident.objects.count()
    total_singles = Resident.objects.filter(status="Single").count()
    total_married = Resident.objects.filter(status="Married").count()
    total_divorced = Resident.objects.filter(status="Divorced").count()
    context = {"total_residents": total_residents, "total_singles": total_singles, "total_divorced": total_divorced, "total_married": total_married}
    return render(request, 'barangayStaff/dashboard.html', context)

def household(request):
    residents = Resident.objects.all()
    residentFilter = ResidentFilters(request.GET, queryset=residents)
    residents = residentFilter.qs
    context = {'residents': residents, 'residentFilter': residentFilter}
    return render(request, 'barangayStaff/household.html', context)

def resident(request):
    residents = Resident.objects.all()
    p = Paginator(residents, 10)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)
    residentFilter = ResidentFilters(request.GET, queryset=residents)
    residents = residentFilter.qs
    context = {'residents': page, 'residentFilter': residentFilter}
    return render(request, 'barangayStaff/resident.html', context)

def settings(request):
    return HttpResponse('Settings')

def logout(request):
    return HttpResponse('Logout')

def view_resident(request, pk):
    resident = Resident.objects.get(id = pk)
    if resident != None:
        return render(request, 'barangayStaff/edit_resident.html', {'editResidents':editResidents})

def add_resident(request):
    if request.method=="POST":
        if request.POST.get('name') \
            and request.POST.get('address') \
            and request.POST.get('birth_date') \
            and request.POST.get('age') \
            and request.POST.get('phone_number') \
            and request.POST.get('gender') \
            and request.POST.get('status') \
            and request.POST.get('vaccination') :
            resident = Resident()
            resident.name = request.POST.get('name')
            resident.address = request.POST.get('address')
            resident.birth_date = request.POST.get('birth_date')
            resident.age = request.POST.get('age')
            resident.phone_number = request.POST.get('phone_number')
            resident.gender = request.POST.get('gender')
            resident.status = request.POST.get('status')
            resident.vaccination = request.POST.get('vaccination')
            resident.save()
            messages.success(request, 'Resident added successfully')
            return HttpResponseRedirect('/resident')
    else:
            return render(request, 'brangayStaff/add_resident.html')

def edit_resident(request, pk):
    resident = get_object_or_404(Resident, id=pk)
    if request.method == "POST":
        resident.name = request.POST.get('name')
        resident.address = request.POST.get('address')
        resident.birth_date = request.POST.get('birth_date')
        resident.age = request.POST.get('age')
        resident.phone_number = request.POST.get('phone_number')
        resident.gender = request.POST.get('gender')
        resident.status = request.POST.get('status')
        resident.vaccination = request.POST.get('vaccination')
        resident.save()
        messages.success(request, 'Resident updated successfully')
        return HttpResponseRedirect('/resident')
    else:
        return render(request, 'edit_resident.html')

def delete_resident(request, pk):
    resident = Resident.objects.get(id=pk)
    resident.delete()
    return HttpResponseRedirect("/resident")
