from django.contrib.auth.models import User
from core.models import Service, Package, Testimonial

# ── Superuser ─────────────────────────────────
User.objects.filter(username='admin').delete()
User.objects.create_superuser('admin', 'admin@blackwood.in', 'admin123')
print("✅ Admin user created  →  username: admin  |  password: admin123")

# ── Services ──────────────────────────────────
services_data = [
    {
        'name': 'Modular Kitchen',
        'category': 'interior',
        'slug': 'modular-kitchen',
        'icon': '🍳',
        'short_desc': 'Custom modular kitchens with premium hardware and finishes.',
        'description': 'Our modular kitchen designs combine functionality with elegance. We use premium laminates, soft-close hardware, quartz countertops, and the finest fittings to create kitchens that are both beautiful and practical.',
        'features': 'Custom Design,Soft-close Hardware,Premium Laminates,Quartz Countertop,Backsplash Tiles,Full Execution',
        'is_featured': True,
        'order': 1,
    },
    {
        'name': 'False Ceiling Design',
        'category': 'interior',
        'slug': 'false-ceiling',
        'icon': '✨',
        'short_desc': 'Designer false ceilings with integrated lighting solutions.',
        'description': 'Transform your rooms with stunning false ceiling designs. From simple gypsum boards to elaborate cove lighting and tray ceilings — we design and execute ceilings that elevate the entire room.',
        'features': 'Gypsum & POP,LED Integration,Cove Lighting,Custom Profiles,Decorative Elements',
        'is_featured': True,
        'order': 2,
    },
    {
        'name': '3D Wallpaper & Wall Panels',
        'category': 'interior',
        'slug': '3d-wallpaper',
        'icon': '🖼️',
        'short_desc': 'Stunning textured and 3D wallpapers that add depth to any room.',
        'description': 'We source premium import-quality wallpapers, textured wall panels, and 3D designs that add personality and drama to your interiors. Available in hundreds of patterns for every style.',
        'features': 'Import Designs,Waterproof Options,Custom Prints,Textured Panels,Easy Maintenance',
        'is_featured': False,
        'order': 3,
    },
    {
        'name': 'Curtains & Motorized Blinds',
        'category': 'interior',
        'slug': 'curtains-blinds',
        'icon': '🪟',
        'short_desc': 'Premium curtains, roller blinds, and motorized solutions.',
        'description': 'Complete your interiors with our range of premium curtains, roller blinds, zebra blinds, and motorized window solutions. We offer custom stitching, premium fabrics, and smart home integration.',
        'features': 'Motorized Blinds,Blackout Options,Custom Stitching,Smart Integration,Premium Fabrics',
        'is_featured': False,
        'order': 4,
    },
    {
        'name': 'Wooden Flooring',
        'category': 'flooring',
        'slug': 'wooden-flooring',
        'icon': '🪵',
        'short_desc': 'Premium engineered and solid hardwood flooring.',
        'description': 'Add warmth and luxury to your space with our premium hardwood flooring. We offer solid wood, engineered wood, and laminate options with various finishes to suit every style and budget.',
        'features': 'Solid & Engineered,Multiple Finishes,Anti-termite Treatment,10 Year Warranty,Expert Installation',
        'is_featured': True,
        'order': 5,
    },
    {
        'name': 'Vinyl Flooring',
        'category': 'flooring',
        'slug': 'vinyl-flooring',
        'icon': '🏁',
        'short_desc': 'Waterproof, durable vinyl flooring for every space.',
        'description': 'Our vinyl flooring solutions are 100% waterproof, scratch-resistant, and available in stunning wood and stone looks. Ideal for kitchens, bathrooms, and commercial spaces.',
        'features': '100% Waterproof,Scratch Resistant,Wood & Stone Look,Easy Maintenance,Commercial Grade',
        'is_featured': False,
        'order': 6,
    },
    {
        'name': 'Epoxy Flooring',
        'category': 'flooring',
        'slug': 'epoxy-flooring',
        'icon': '🔵',
        'short_desc': 'Seamless, high-gloss epoxy floors for a sleek aesthetic.',
        'description': 'Epoxy flooring offers a seamless, high-gloss surface that is both stunning and extremely durable. Available in solid colors, metallic effects, and custom patterns for residential and commercial use.',
        'features': 'Seamless Finish,Chemical Resistant,Custom Colors,Metallic Options,Anti-slip Coating',
        'is_featured': False,
        'order': 7,
    },
    {
        'name': 'House Construction',
        'category': 'construction',
        'slug': 'house-construction',
        'icon': '🏗️',
        'short_desc': 'End-to-end home construction with the finest materials.',
        'description': 'From foundation to finishing, we manage your entire home construction project with complete transparency and accountability. Our experienced team ensures quality at every stage.',
        'features': 'Foundation to Finish,Structural Planning,Quality Materials,DTCP Approval,Timeline Guarantee',
        'is_featured': True,
        'order': 8,
    },
    {
        'name': 'Elevation Design',
        'category': 'construction',
        'slug': 'elevation-design',
        'icon': '🏛️',
        'short_desc': 'Stunning façade designs that make your home stand out.',
        'description': 'Your home\'s exterior is its first impression. Our elevation designers create stunning façades using a mix of textures, materials, and lighting to give your home a unique, memorable identity.',
        'features': '3D Visualization,Modern & Classic Styles,Material Selection,Lighting Design,Execution Support',
        'is_featured': False,
        'order': 9,
    },
    {
        'name': 'DTCP Approval',
        'category': 'construction',
        'slug': 'dtcp-approval',
        'icon': '📋',
        'short_desc': 'Complete legal approval support from planning to clearance.',
        'description': 'We handle the entire DTCP approval process — from architectural plan preparation to submission and final clearance. Our team ensures full legal compliance so you can build with confidence.',
        'features': 'Plan Preparation,Approval Submission,Legal Compliance,Liaison Support,Documentation',
        'is_featured': False,
        'order': 10,
    },
    {
        'name': 'Landscape Design',
        'category': 'outdoor',
        'slug': 'landscape-design',
        'icon': '🌿',
        'short_desc': 'Transform outdoor spaces with lush landscape design.',
        'description': 'Beautiful landscapes that complement your architecture. We design and execute gardens, pathways, water features, and outdoor living spaces that are both beautiful and functional.',
        'features': 'Garden Planning,Hardscape Design,Irrigation Systems,Plant Selection,Lighting Design',
        'is_featured': True,
        'order': 11,
    },
    {
        'name': 'Netlon Installation',
        'category': 'outdoor',
        'slug': 'netlon-installation',
        'icon': '🦟',
        'short_desc': 'High-quality mosquito protection for windows and balconies.',
        'description': 'Protect your home from mosquitoes and insects with our premium Netlon installation. We fit high-quality UV-resistant nets on windows, doors, and balconies without blocking airflow or light.',
        'features': 'All Window Types,UV Resistant,Easy Maintenance,Invisible Design,Long Lasting',
        'is_featured': False,
        'order': 12,
    },
    {
        'name': 'Vastu Consultation',
        'category': 'consultation',
        'slug': 'vastu-consultation',
        'icon': '🧭',
        'short_desc': 'Expert Vastu guidance integrated with modern design.',
        'description': 'Our Vastu experts provide personalized consultations that align your living spaces with natural energies. We integrate traditional Vastu principles seamlessly into modern design without compromising aesthetics.',
        'features': 'Direction Analysis,Space Optimization,Energy Flow,Personalized Report,Design Integration',
        'is_featured': True,
        'order': 13,
    },
    {
        'name': 'Design Consultation',
        'category': 'consultation',
        'slug': 'design-consultation',
        'icon': '💡',
        'short_desc': 'One-on-one design sessions to plan your dream space.',
        'description': 'Sit down with our senior designers for a focused consultation session. We\'ll understand your style, requirements, and budget — then create a mood board, space plan, and detailed design brief just for you.',
        'features': 'Mood Board Creation,3D Visualization,Budget Planning,Material Selection,Style Guide',
        'is_featured': False,
        'order': 14,
    },
]

for s in services_data:
    Service.objects.get_or_create(slug=s['slug'], defaults=s)

print(f"✅ Services created  →  {Service.objects.count()} total")

# ── Packages ──────────────────────────────────
packages_data = [
    {
        'name': '2BHK Starter',
        'subtitle': 'Perfect for compact homes',
        'description': 'Smart, stylish design for 2BHK apartments up to 800 sq.ft.',
        'price_starting': 1200,
        'price_unit': 'per sq.ft',
        'inclusions': 'Living & Dining Design,2 Bedroom Interiors,Basic Modular Kitchen,False Ceiling (2 rooms),Wardrobe (2 units),TV Unit,Paint & Wallpaper,Electrical Work',
        'is_popular': False,
        'order': 1,
    },
    {
        'name': 'Full Home Premium',
        'subtitle': 'Complete transformation — best value',
        'description': 'Head-to-toe redesign for 3BHK homes with premium finishes.',
        'price_starting': 1800,
        'price_unit': 'per sq.ft',
        'inclusions': 'All Rooms Designed,Premium Modular Kitchen,Engineered Wood Flooring,Designer False Ceiling,Custom Wardrobes (all rooms),Crockery Unit,3D Visualization,Vastu Consultation,Project Manager Assigned',
        'is_popular': True,
        'order': 2,
    },
    {
        'name': 'Luxury Villa',
        'subtitle': 'Ultra-premium, no-compromise design',
        'description': 'For those who demand only the finest — imported materials and bespoke craftsmanship.',
        'price_starting': 2500,
        'price_unit': 'per sq.ft',
        'inclusions': 'Full Interior + Architecture,Imported Materials,Smart Home Integration,Landscape Design,Video Walkthrough,Dedicated Senior Designer,Post-completion Support,2-Year Warranty',
        'is_popular': False,
        'order': 3,
    },
]

for p in packages_data:
    Package.objects.get_or_create(name=p['name'], defaults=p)

print(f"✅ Packages created   →  {Package.objects.count()} total")

# ── Testimonials ──────────────────────────────
testimonials_data = [
    {
        'client_name': 'Rajan Sharma',
        'location': 'Chennai',
        'project_type': 'Full Home Interior',
        'review': 'Black Wood Interiors transformed our villa beyond expectations. Every corner feels intentional and luxurious. The team was professional, punctual, and delivered exactly what was promised.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'client_name': 'Kavitha Nair',
        'location': 'Bangalore',
        'project_type': 'Modular Kitchen',
        'review': 'Our kitchen is magazine-worthy! The team handled the entire design and execution in 3 weeks. Absolutely stunning result — we get compliments from every guest.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'client_name': 'Priya Sundaram',
        'location': 'Chennai',
        'project_type': '3BHK Renovation',
        'review': 'From Vastu consultation to final handover, the entire process was seamless. The 3D designs helped us visualize everything perfectly before any work began.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'client_name': 'Arvind Kumar',
        'location': 'Chennai',
        'project_type': 'House Construction',
        'review': 'They managed our entire construction with complete transparency. Budget was respected, timeline was met. I would recommend Black Wood Interiors to anyone building a home.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'client_name': 'Meena Krishnan',
        'location': 'Bangalore',
        'project_type': 'Flooring & False Ceiling',
        'review': 'Exceptional craftsmanship on our wooden flooring and false ceiling. The house looks like a luxury hotel now. Worth every rupee — and the team was a pleasure to work with.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'client_name': 'Suresh Balaji',
        'location': 'Chennai',
        'project_type': 'Landscape Design',
        'review': 'Our garden has been completely transformed. The landscape team designed something truly beautiful — neighbours constantly ask who did the work. Highly satisfied!',
        'rating': 5,
        'is_featured': True,
    },
]

for t in testimonials_data:
    Testimonial.objects.get_or_create(client_name=t['client_name'], defaults=t)

print(f"✅ Testimonials created →  {Testimonial.objects.count()} total")
print()
print("━" * 50)
print("🏡 BLACK WOOD INTERIORS — Setup Complete!")
print("━" * 50)
print("  Admin URL  →  http://localhost:8000/admin/")
print("  Username   →  admin")
print("  Password   →  admin123")
print("━" * 50)
