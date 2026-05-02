from django.conf import settings

def site_settings(request):
    return {
        'whatsapp_number': getattr(settings, 'WHATSAPP_NUMBER', '919876543210'),
        'site_name': 'Black Wood Interiors',
    }
