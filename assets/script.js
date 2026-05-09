// ============= NEGOCE RATIONEL — Interactions =============

function applyLanguage(lang) {
  if (!window.I18N || !window.I18N[lang]) return;
  const dict = window.I18N[lang];

  document.querySelectorAll('[data-i18n]').forEach((el) => {
    const key = el.getAttribute('data-i18n');
    if (dict[key] !== undefined) el.textContent = dict[key];
  });

  document.querySelectorAll('[data-i18n-placeholder]').forEach((el) => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (dict[key] !== undefined) el.setAttribute('placeholder', dict[key]);
  });

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

  document.querySelectorAll('.lang-btn').forEach((btn) => {
    const isActive = btn.dataset.lang === lang;
    btn.classList.toggle('bg-brand-600', isActive);
    btn.classList.toggle('text-white', isActive);
    btn.classList.toggle('text-steel-700', !isActive);
    btn.setAttribute('aria-pressed', String(isActive));
  });

  try { localStorage.setItem('negoce-lang', lang); } catch (_) {}
}

document.addEventListener('DOMContentLoaded', () => {
  // ----- AOS init -----
  if (window.AOS) {
    AOS.init({
      duration: 800,
      easing: 'ease-out-cubic',
      once: true,
      offset: 60,
      disable: () => window.matchMedia('(prefers-reduced-motion: reduce)').matches,
    });
  }

  // ----- Language switcher (URL ?lang= override + localStorage) -----
  document.querySelectorAll('.lang-btn').forEach((btn) => {
    btn.addEventListener('click', () => applyLanguage(btn.dataset.lang));
  });
  const urlLang = new URLSearchParams(window.location.search).get('lang');
  let savedLang = 'fr';
  try { savedLang = localStorage.getItem('negoce-lang') || 'fr'; } catch (_) {}
  applyLanguage((urlLang === 'fr' || urlLang === 'ar') ? urlLang : savedLang);

  // ----- Mobile menu -----
  const menuToggle = document.getElementById('menuToggle');
  const mobileMenu = document.getElementById('mobileMenu');
  if (menuToggle && mobileMenu) {
    const setOpen = (open) => {
      mobileMenu.classList.toggle('hidden', !open);
      menuToggle.setAttribute('aria-expanded', String(open));
      const icon = menuToggle.querySelector('i');
      if (icon) {
        icon.classList.toggle('fa-bars', !open);
        icon.classList.toggle('fa-xmark', open);
      }
    };
    menuToggle.addEventListener('click', () => {
      const isOpen = !mobileMenu.classList.contains('hidden');
      setOpen(!isOpen);
    });
    mobileMenu.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => setOpen(false))
    );
    // close on Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) setOpen(false);
    });
  }

  // ----- Navbar scroll effect + back-to-top -----
  const navbar = document.getElementById('navbar');
  const backToTop = document.getElementById('backToTop');
  const onScroll = () => {
    if (!navbar) return;
    if (window.scrollY > 30) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');

    if (backToTop) {
      const show = window.scrollY > 600;
      backToTop.classList.toggle('hidden', !show);
      backToTop.classList.toggle('flex', show);
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
    const target = parseInt(el.dataset.target, 10) || 0;
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
      if (id && id.length > 1 && id !== '#') {
        const target = document.querySelector(id);
        if (target) {
          e.preventDefault();
          const offset = 80;
          const top = target.getBoundingClientRect().top + window.scrollY - offset;
          window.scrollTo({ top, behavior: 'smooth' });
          // accessibility: move focus
          target.setAttribute('tabindex', '-1');
          target.focus({ preventScroll: true });
        }
      }
    });
  });

  // ----- Pre-select product in form when clicking product CTA -----
  document.querySelectorAll('a[href="#contact"][data-product]').forEach((a) => {
    a.addEventListener('click', () => {
      const wanted = a.getAttribute('data-product');
      const select = document.getElementById('f-product');
      if (!select || !wanted) return;
      const opts = select.querySelectorAll('option');
      let matched = false;
      opts.forEach((opt) => {
        if (opt.textContent.trim().toLowerCase().includes(wanted.toLowerCase().split(' ')[0])) {
          if (!matched) { opt.selected = true; matched = true; }
        }
      });
    });
  });

  // ----- Contact form (mailto fallback + validation + honeypot) -----
  const form = document.getElementById('contactForm');
  const formMsg = document.getElementById('formMsg');
  const dict = () => (window.I18N && window.I18N[document.documentElement.lang]) || {};

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const honeypot = (data.get('website') || '').toString().trim();
      if (honeypot) return; // bot trap

      const name = (data.get('name') || '').toString().trim();
      const email = (data.get('email') || '').toString().trim();
      const phone = (data.get('phone') || '').toString().trim();
      const product = (data.get('product') || '').toString().trim();
      const message = (data.get('message') || '').toString().trim();

      const showMsg = (text, ok = true) => {
        if (!formMsg) return;
        formMsg.textContent = text;
        formMsg.className = `text-sm text-center font-semibold ${ok ? 'text-brand-700' : 'text-red-600'}`;
        formMsg.classList.remove('hidden');
      };

      if (!name || !email) {
        showMsg(dict()['form.err.required'] || 'Merci de remplir les champs obligatoires.', false);
        return;
      }
      const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRe.test(email)) {
        showMsg(dict()['form.err.email'] || 'Adresse email invalide.', false);
        return;
      }

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

      showMsg(dict()['form.ok'] || '✓ Votre client mail s\'ouvre.', true);
    });
  }

  // ----- Product card subtle 3D tilt on mouse move (skipped on touch & reduced motion) -----
  const supportsHover = window.matchMedia('(hover: hover)').matches;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (supportsHover && !reducedMotion) {
    document.querySelectorAll('.product-card').forEach((card) => {
      const inner = card.firstElementChild;
      if (!inner) return;
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
  }

  // ----- FAQ : single-open accordion behavior -----
  const faqList = document.getElementById('faqList');
  if (faqList) {
    faqList.querySelectorAll('details.faq-item').forEach((d) => {
      d.addEventListener('toggle', () => {
        if (d.open) {
          faqList.querySelectorAll('details.faq-item').forEach((other) => {
            if (other !== d) other.open = false;
          });
        }
      });
    });
  }
});
