from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Service, Project, Package, Testimonial, Lead, Booking
from .forms import LeadForm, BookingForm, QuotationForm
import json


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    services = Service.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_featured=True)[:6]
    packages = Package.objects.all()[:3]
    lead_form = LeadForm()
    context = {
        'featured_projects': featured_projects,
        'services': services,
        'testimonials': testimonials,
        'packages': packages,
        'lead_form': lead_form,
    }
    return render(request, 'home.html', context)


def services(request):
    all_services = Service.objects.all()
    categories = {}
    for svc in all_services:
        cat = svc.get_category_display()
        categories.setdefault(cat, []).append(svc)
    return render(request, 'services.html', {'categories': categories, 'services': all_services})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related = Service.objects.filter(category=service.category).exclude(id=service.id)[:3]
    projects = Project.objects.filter(category=service.category)[:6]
    return render(request, 'service_detail.html', {'service': service, 'related': related, 'projects': projects})


def portfolio(request):
    category = request.GET.get('category', '')
    projects = Project.objects.all()
    if category:
        projects = projects.filter(category=category)
    categories = Project.objects.values_list('category', flat=True).distinct()
    return render(request, 'portfolio.html', {
        'projects': projects,
        'categories': categories,
        'active_category': category,
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    related = Project.objects.filter(category=project.category).exclude(pk=pk)[:4]
    return render(request, 'project_detail.html', {'project': project, 'related': related})


def consultation(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your consultation has been booked! We will contact you shortly.')
            return redirect('consultation')
    else:
        form = BookingForm()
    return render(request, 'consultation.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! We will call you back within 24 hours.')
            return redirect('contact')
    else:
        form = LeadForm()
    return render(request, 'contact.html', {'form': form})


def packages(request):
    all_packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': all_packages})


def quotation(request):
    estimated = None
    service_label = ''
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            rate_map = {
                'modular_kitchen': 1200, 'false_ceiling': 85, 'full_interior': 1800,
                'wooden_flooring': 180, 'vinyl_flooring': 120, 'epoxy_flooring': 150,
                'house_construction': 2200,
            }
            rate = rate_map.get(obj.service_type, 1000)
            obj.estimated_cost = rate * obj.area_sqft
            obj.save()
            estimated = obj.estimated_cost
            service_label = obj.service_type.replace('_', ' ').title()
    else:
        form = QuotationForm()
    return render(request, 'quotation.html', {'form': form, 'estimated': estimated, 'service_label': service_label})


def submit_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Thank you! We will call you soon.'})
            messages.success(request, 'Thank you! We will call you back.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return JsonResponse({'success': False}, status=400)
