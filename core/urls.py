from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:pk>/', views.project_detail, name='project_detail'),
    path('consultation/', views.consultation, name='consultation'),
    path('contact/', views.contact, name='contact'),
    path('packages/', views.packages, name='packages'),
    path('quotation/', views.quotation, name='quotation'),
    path('submit-lead/', views.submit_lead, name='submit_lead'),
]
