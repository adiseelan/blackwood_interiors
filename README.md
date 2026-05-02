# 🏡 Black Wood Interiors — Django Website

Luxury Interior Design & Architecture website built with Django.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install django pillow

# 2. Run migrations
python manage.py migrate

# 3. Create superuser (or use existing: admin / admin123)
python manage.py createsuperuser

# 4. Load seed data (services, packages, testimonials)
python manage.py shell < seed.py   # or run the shell commands from setup

# 5. Start server
python manage.py runserver
```

Visit: http://localhost:8000

## 🔐 Admin Panel
URL: http://localhost:8000/admin/
Username: admin | Password: admin123

## 📄 Pages
| Page | URL |
|------|-----|
| Home | / |
| Services | /services/ |
| Service Detail | /services/<slug>/ |
| Portfolio | /portfolio/ |
| Project Detail | /portfolio/<id>/ |
| Packages | /packages/ |
| Quotation | /quotation/ |
| Consultation | /consultation/ |
| Contact | /contact/ |

## 🎨 Design
- **Colors:** Black `#0a0a0a`, White, Gold `#c9a84c`, Cream `#f5f0e8`
- **Fonts:** Cormorant Garamond (serif) + Jost (sans)
- **Style:** Luxury minimal, smooth animations, fully responsive

## ⚙️ Customize
1. **WhatsApp number** → `blackwood/settings.py` → `WHATSAPP_NUMBER`
2. **Services/Packages** → Admin panel → Add via Django admin
3. **Portfolio projects** → Admin panel → Upload project images
4. **Contact info** → Edit `templates/base.html` footer section

## 📦 Models
- `Service` — Services with categories, features, slugs
- `Project` — Portfolio projects with before/after images
- `Package` — Pricing packages with inclusions
- `Testimonial` — Client reviews
- `Lead` — Enquiry form submissions (tracked in admin)
- `Booking` — Consultation bookings (with status tracking)
- `QuotationRequest` — Auto-calculated estimates

## 🌐 Production Deployment
1. Set `DEBUG = False` in settings.py
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Run `python manage.py collectstatic`
5. Use Gunicorn + Nginx
