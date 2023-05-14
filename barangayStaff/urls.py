from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.dashboard, name='dashboard'),
    path('household/', views.household, name='household'),
    path('resident/', views.resident, name='resident'),
    path('settings/', views.settings),
    path('logout/', views.logout),
    path('create_resident/', views.createResident, name='create_resident'),
    path('view_resident/<str:pk>/', views.view_resident, name='view_resident'),
    path('update_resident/<str:pk>/', views.updateResident, name='update_resident'),
    path('delete_resident/<str:pk>/', views.deleteResident, name='delete_resident'),
]
