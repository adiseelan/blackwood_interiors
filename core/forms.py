from django import forms
from .models import Lead, Booking, QuotationRequest, BUDGET_CHOICES, TIME_SLOTS, SERVICE_CATEGORIES


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone', 'email', 'location', 'service', 'budget', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address (optional)', 'class': 'form-input'}),
            'location': forms.TextInput(attrs={'placeholder': 'City / Area', 'class': 'form-input'}),
            'service': forms.TextInput(attrs={'placeholder': 'Service Interested In', 'class': 'form-input'}),
            'budget': forms.Select(attrs={'class': 'form-input form-select'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about your project...', 'class': 'form-input form-textarea', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['budget'].empty_label = 'Select Budget Range'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email', 'service', 'date', 'time_slot', 'location', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email (optional)', 'class': 'form-input'}),
            'service': forms.TextInput(attrs={'placeholder': 'Service Required', 'class': 'form-input'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'time_slot': forms.Select(attrs={'class': 'form-input form-select'}),
            'location': forms.TextInput(attrs={'placeholder': 'Your Location', 'class': 'form-input'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Additional notes...', 'class': 'form-input form-textarea', 'rows': 3}),
        }


class QuotationForm(forms.ModelForm):
    STYLE_CHOICES = [
        ('', 'Select Style'),
        ('modern', 'Modern'),
        ('luxury', 'Luxury'),
        ('minimal', 'Minimal'),
        ('traditional', 'Traditional'),
        ('contemporary', 'Contemporary'),
    ]
    SERVICE_CHOICES = [
        ('', 'Select Service'),
        ('modular_kitchen', 'Modular Kitchen'),
        ('false_ceiling', 'False Ceiling'),
        ('full_interior', 'Full Interior Design'),
        ('wooden_flooring', 'Wooden Flooring'),
        ('vinyl_flooring', 'Vinyl Flooring'),
        ('epoxy_flooring', 'Epoxy Flooring'),
        ('house_construction', 'House Construction'),
    ]
    RATE_PER_SQFT = {
        'modular_kitchen': 1200,
        'false_ceiling': 85,
        'full_interior': 1800,
        'wooden_flooring': 180,
        'vinyl_flooring': 120,
        'epoxy_flooring': 150,
        'house_construction': 2200,
    }
    SERVICE_CHOICES = [
        ('', 'Select Service'),
        ('modular_kitchen', 'Modular Kitchen'),
        ('false_ceiling', 'False Ceiling'),
        ('full_interior', 'Full Interior Design'),
        ('wooden_flooring', 'Wooden Flooring'),
        ('vinyl_flooring', 'Vinyl Flooring'),
        ('epoxy_flooring', 'Epoxy Flooring'),
        ('house_construction', 'House Construction'),
    ]
    style = forms.ChoiceField(choices=STYLE_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-input form-select'}))

    class Meta:
        model = QuotationRequest
        fields = ['name', 'phone', 'service_type', 'area_sqft', 'style']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-input'}),
            'service_type': forms.Select(attrs={'class': 'form-input form-select', 'id': 'id_service_type'}),
            'area_sqft': forms.NumberInput(attrs={'placeholder': 'Area in Sq.ft', 'class': 'form-input', 'min': '1'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service_type'].widget.choices = self.SERVICE_CHOICES
