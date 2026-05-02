/* BLACK WOOD INTERIORS — Main JS */

document.addEventListener('DOMContentLoaded', () => {

  // ── NAVBAR SCROLL ─────────────────────────
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    navbar?.classList.toggle('scrolled', window.scrollY > 60);
  });

  // ── MOBILE MENU ───────────────────────────
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  hamburger?.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    const isOpen = mobileMenu?.classList.contains('open');
    if (isOpen) {
        mobileMenu.classList.remove('open');
        mobileMenu.style.display = 'none';
        document.body.style.overflow = '';
    } else {
        mobileMenu.style.display = 'flex';
        setTimeout(() => mobileMenu?.classList.add('open'), 10);
        document.body.style.overflow = 'hidden';
    }
});
 mobileMenu?.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger?.classList.remove('open');
      mobileMenu.classList.remove('open');
      mobileMenu.style.display = 'none';
      document.body.style.overflow = '';
    });
});

  // ── SCROLL REVEAL ─────────────────────────
  const reveals = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); } });
  }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
  reveals.forEach(el => revealObserver.observe(el));

  // ── ACTIVE NAV LINK ───────────────────────
  const path = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(a => {
    if (a.getAttribute('href') === path || (path !== '/' && a.getAttribute('href')?.startsWith(path.split('/')[1]))) {
      a.classList.add('active');
    }
  });

  // ── PORTFOLIO FILTER ──────────────────────
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const cat = btn.dataset.category;
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (cat === 'all') {
        window.location.href = '/portfolio/';
      } else {
        window.location.href = `/portfolio/?category=${cat}`;
      }
    });
  });

  // ── COUNTER ANIMATION ─────────────────────
  const counters = document.querySelectorAll('.counter');
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const el = e.target;
        const target = parseInt(el.dataset.target);
        let count = 0;
        const step = target / 60;
        const timer = setInterval(() => {
          count += step;
          if (count >= target) { el.textContent = target; clearInterval(timer); }
          else { el.textContent = Math.floor(count); }
        }, 20);
        counterObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach(el => counterObserver.observe(el));

  // ── QUOTATION CALCULATOR ──────────────────
  const serviceSelect = document.querySelector('#id_service_type');
  const areaInput = document.querySelector('#id_area_sqft');
  const liveResult = document.querySelector('#live-estimate');
  const rates = {
    'modular_kitchen': 1200, 'false_ceiling': 85, 'full_interior': 1800,
    'wooden_flooring': 180, 'vinyl_flooring': 120, 'epoxy_flooring': 150,
    'house_construction': 2200,
  };
  function updateEstimate() {
    if (!serviceSelect || !areaInput || !liveResult) return;
    const service = serviceSelect.value;
    const area = parseInt(areaInput.value);
    if (service && area && rates[service]) {
      const cost = rates[service] * area;
      liveResult.textContent = '₹' + cost.toLocaleString('en-IN');
      liveResult.closest('.live-estimate-box')?.classList.remove('hidden');
    }
  }
  serviceSelect?.addEventListener('change', updateEstimate);
  areaInput?.addEventListener('input', updateEstimate);

  // ── LEAD FORM AJAX ─────────────────────────
  const leadForms = document.querySelectorAll('.ajax-lead-form');
  leadForms.forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('[type="submit"]');
      const originalText = btn.textContent;
      btn.textContent = 'Sending…';
      btn.disabled = true;
      try {
        const res = await fetch('/submit-lead/', {
          method: 'POST',
          body: new FormData(form),
          headers: { 'X-Requested-With': 'XMLHttpRequest' },
        });
        const data = await res.json();
        if (data.success) {
          form.innerHTML = `<div class="alert alert-success" style="margin:0">
            ✓ ${data.message || 'Thank you! We will call you soon.'}
          </div>`;
        }
      } catch {
        btn.textContent = originalText;
        btn.disabled = false;
      }
    });
  });

  // ── SMOOTH ANCHOR SCROLL ──────────────────
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ── BOOKING DATE MIN ──────────────────────
  const dateInput = document.querySelector('input[type="date"]');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;
  }

  // ── BEFORE/AFTER SLIDER ───────────────────
  const sliders = document.querySelectorAll('.ba-slider');
  sliders.forEach(slider => {
    const handle = slider.querySelector('.ba-handle');
    const after = slider.querySelector('.ba-after');
    let dragging = false;
    const move = (clientX) => {
      const rect = slider.getBoundingClientRect();
      const pct = Math.max(0, Math.min(100, ((clientX - rect.left) / rect.width) * 100));
      after.style.clipPath = `inset(0 ${100 - pct}% 0 0)`;
      handle.style.left = pct + '%';
    };
    handle?.addEventListener('mousedown', () => dragging = true);
    window.addEventListener('mousemove', e => { if (dragging) move(e.clientX); });
    window.addEventListener('mouseup', () => dragging = false);
    handle?.addEventListener('touchstart', () => dragging = true, { passive: true });
    window.addEventListener('touchmove', e => { if (dragging) move(e.touches[0].clientX); }, { passive: true });
    window.addEventListener('touchend', () => dragging = false);
  });

});
