from django.db import models


SERVICE_CATEGORIES = [
    ('interior', 'Interior Design & Execution'),
    ('flooring', 'Flooring Solutions'),
    ('construction', 'Construction & Architecture'),
    ('outdoor', 'Outdoor & Utility Services'),
    ('consultation', 'Planning & Consultation'),
]

PROJECT_CATEGORIES = [
    ('interiors', 'Interiors'),
    ('construction', 'Construction'),
    ('flooring', 'Flooring'),
    ('kitchen', 'Modular Kitchen'),
    ('outdoor', 'Outdoor'),
]

BUDGET_CHOICES = [
    ('below_5', 'Below ₹5 Lakhs'),
    ('5_10', '₹5 – ₹10 Lakhs'),
    ('10_25', '₹10 – ₹25 Lakhs'),
    ('25_50', '₹25 – ₹50 Lakhs'),
    ('above_50', 'Above ₹50 Lakhs'),
]

TIME_SLOTS = [
    ('10:00', '10:00 AM'),
    ('11:00', '11:00 AM'),
    ('12:00', '12:00 PM'),
    ('14:00', '02:00 PM'),
    ('15:00', '03:00 PM'),
    ('16:00', '04:00 PM'),
    ('17:00', '05:00 PM'),
]


class Service(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=SERVICE_CATEGORIES)
    description = models.TextField()
    short_desc = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=10, blank=True, help_text='Emoji or icon class')
    icon_image = models.ImageField(upload_to='services/icons/', null=True, blank=True)
    features = models.TextField(blank=True, help_text='Comma-separated features')
    slug = models.SlugField(unique=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_features_list(self):
        return [f.strip() for f in self.features.split(',') if f.strip()]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=PROJECT_CATEGORIES)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    area_sqft = models.PositiveIntegerField(null=True, blank=True)
    main_image = models.ImageField(upload_to='projects/', null=True, blank=True)
    before_image = models.ImageField(upload_to='projects/before/', null=True, blank=True)
    after_image = models.ImageField(upload_to='projects/after/', null=True, blank=True)
    video_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    completed_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class Package(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    price_starting = models.DecimalField(max_digits=12, decimal_places=2)
    price_unit = models.CharField(max_length=50, default='per sq.ft')
    inclusions = models.TextField(help_text='Comma-separated list')
    is_popular = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_inclusions_list(self):
        return [i.strip() for i in self.inclusions.split(',') if i.strip()]

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    project_type = models.CharField(max_length=100, blank=True)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    photo = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} – {self.project_type}"


class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('closed', 'Closed'),
        ('lost', 'Lost'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=100, blank=True)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    source = models.CharField(max_length=50, default='website')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} – {self.phone}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    service = models.CharField(max_length=100)
    date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=TIME_SLOTS)
    location = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'time_slot']

    def __str__(self):
        return f"{self.name} – {self.date} {self.time_slot}"


class QuotationRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    service_type = models.CharField(max_length=100)
    area_sqft = models.PositiveIntegerField()
    style = models.CharField(max_length=50, blank=True)
    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote – {self.name} ({self.area_sqft} sqft)"
