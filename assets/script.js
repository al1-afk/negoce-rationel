// ============= NEGOCE RATIONEL — Interactions =============

// ----- i18n: Language switching (FR / AR) -----
function applyLanguage(lang) {
  if (!window.I18N || !window.I18N[lang]) return;
  const dict = window.I18N[lang];

  // Translate text content
  document.querySelectorAll('[data-i18n]').forEach((el) => {
    const key = el.getAttribute('data-i18n');
    if (dict[key] !== undefined) el.textContent = dict[key];
  });

  // Translate placeholders
  document.querySelectorAll('[data-i18n-placeholder]').forEach((el) => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (dict[key] !== undefined) el.setAttribute('placeholder', dict[key]);
  });

  // Direction & font
  const html = document.documentElement;
  if (lang === 'ar') {
    html.setAttribute('lang', 'ar');
    html.setAttribute('dir', 'rtl');
    document.body.classList.add('lang-ar');
  } else {
    html.setAttribute('lang', 'fr');
    html.setAttribute('dir', 'ltr');
    document.body.classList.remove('lang-ar');
  }

  // Update active button state
  document.querySelectorAll('.lang-btn').forEach((btn) => {
    if (btn.dataset.lang === lang) {
      btn.classList.add('bg-brand-600', 'text-white');
      btn.classList.remove('text-steel-700');
    } else {
      btn.classList.remove('bg-brand-600', 'text-white');
      btn.classList.add('text-steel-700');
    }
  });

  localStorage.setItem('negoce-lang', lang);
}

document.addEventListener('DOMContentLoaded', () => {
  // ----- AOS init -----
  if (window.AOS) {
    AOS.init({
      duration: 800,
      easing: 'ease-out-cubic',
      once: true,
      offset: 60,
    });
  }

  // ----- Language switcher -----
  document.querySelectorAll('.lang-btn').forEach((btn) => {
    btn.addEventListener('click', () => applyLanguage(btn.dataset.lang));
  });
  const savedLang = localStorage.getItem('negoce-lang') || 'fr';
  applyLanguage(savedLang);

  // ----- Mobile menu -----
  const menuToggle = document.getElementById('menuToggle');
  const mobileMenu = document.getElementById('mobileMenu');
  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
      const icon = menuToggle.querySelector('i');
      icon.classList.toggle('fa-bars');
      icon.classList.toggle('fa-xmark');
    });
    mobileMenu.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => mobileMenu.classList.add('hidden'))
    );
  }

  // ----- Navbar scroll effect -----
  const navbar = document.getElementById('navbar');
  const backToTop = document.getElementById('backToTop');
  const onScroll = () => {
    if (window.scrollY > 30) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');

    if (window.scrollY > 600) {
      backToTop.classList.remove('hidden');
      backToTop.classList.add('flex');
    } else {
      backToTop.classList.add('hidden');
      backToTop.classList.remove('flex');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (backToTop) {
    backToTop.addEventListener('click', () =>
      window.scrollTo({ top: 0, behavior: 'smooth' })
    );
  }

  // ----- Counter animation -----
  const counters = document.querySelectorAll('.counter');
  const animateCounter = (el) => {
    const target = parseInt(el.dataset.target, 10);
    const duration = 1800;
    const startTime = performance.now();
    const easeOut = (t) => 1 - Math.pow(1 - t, 3);

    const tick = (now) => {
      const progress = Math.min((now - startTime) / duration, 1);
      const value = Math.floor(easeOut(progress) * target);
      el.textContent = value.toLocaleString('fr-FR');
      if (progress < 1) requestAnimationFrame(tick);
      else el.textContent = target.toLocaleString('fr-FR');
    };
    requestAnimationFrame(tick);
  };

  if ('IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });
    counters.forEach((c) => counterObserver.observe(c));
  } else {
    counters.forEach(animateCounter);
  }

  // ----- Smooth anchor scroll (offset for sticky navbar) -----
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href');
      if (id.length > 1) {
        const target = document.querySelector(id);
        if (target) {
          e.preventDefault();
          const offset = 80;
          const top = target.getBoundingClientRect().top + window.scrollY - offset;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      }
    });
  });

  // ----- Contact form (mailto fallback) -----
  const form = document.getElementById('contactForm');
  const formMsg = document.getElementById('formMsg');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const name = data.get('name') || '';
      const email = data.get('email') || '';
      const phone = data.get('phone') || '';
      const product = data.get('product') || '';
      const message = data.get('message') || '';

      const subject = `Demande de devis — ${product}`;
      const body =
        `Bonjour,\n\n` +
        `Je souhaite obtenir un devis pour : ${product}\n\n` +
        `Nom : ${name}\n` +
        `Téléphone : ${phone}\n` +
        `Email : ${email}\n\n` +
        `Message :\n${message}\n\n` +
        `Cordialement,\n${name}`;

      const mailto = `mailto:negocerationel@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      window.location.href = mailto;

      formMsg.textContent = '✓ Votre message est prêt à être envoyé. Vérifiez votre client mail.';
      formMsg.className = 'text-sm text-center text-brand-700 font-semibold';
      formMsg.classList.remove('hidden');
    });
  }

  // ----- Product card subtle 3D tilt on mouse move -----
  const cards = document.querySelectorAll('.product-card');
  cards.forEach((card) => {
    const inner = card.firstElementChild;
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width - 0.5) * 6;
      const y = ((e.clientY - rect.top) / rect.height - 0.5) * -6;
      inner.style.transform = `perspective(1000px) rotateX(${y}deg) rotateY(${x}deg) translateY(-4px)`;
    });
    card.addEventListener('mouseleave', () => {
      inner.style.transform = '';
    });
  });
});
