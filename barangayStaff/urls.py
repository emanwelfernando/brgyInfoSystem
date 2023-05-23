from django.urls import path
from django.contrib import admin
from barangayStaff import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.dashboard, name='dashboard'),
    path('household/', views.household, name='household'),
    path('resident/', views.resident, name='resident'),
    path('settings/', views.settings),
    path('logout/', views.logout),
    path('add_resident', views.add_resident, name='add_resident'),
    path('view_resident/<str:pk>/', views.view_resident, name='view_resident'),
    path('edit_resident/<str:pk>/', views.edit_resident, name='edit_resident'),
    path('delete_resident/<str:pk>/', views.delete_resident, name='delete_resident'),
]
