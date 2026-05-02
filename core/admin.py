from django.contrib import admin
from .models import Service, Project, ProjectImage, Package, Testimonial, Lead, Booking, QuotationRequest

admin.site.site_header = "Black Wood Interiors Admin"
admin.site.site_title = "BWI Admin"
admin.site.index_title = "Dashboard"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']
    list_editable = ['is_featured', 'order']
    prepopulated_fields = {'slug': ('name',)}


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'location', 'is_featured', 'completed_date']
    list_filter = ['category', 'is_featured']
    list_editable = ['is_featured']
    inlines = [ProjectImageInline]


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_starting', 'price_unit', 'is_popular', 'order']
    list_editable = ['is_popular', 'order']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'location', 'project_type', 'rating', 'is_featured']
    list_editable = ['is_featured']


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'budget', 'status', 'created_at']
    list_filter = ['status', 'budget']
    list_editable = ['status']
    readonly_fields = ['created_at']
    search_fields = ['name', 'phone', 'location']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'date', 'time_slot', 'status']
    list_filter = ['status', 'date']
    list_editable = ['status']
    readonly_fields = ['created_at']


@admin.register(QuotationRequest)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service_type', 'area_sqft', 'estimated_cost', 'created_at']
    readonly_fields = ['estimated_cost', 'created_at']
