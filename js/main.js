// TextGenetic AI — lightweight interactions (no dependencies)
(function () {
  document.documentElement.classList.add('js');

  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('nav');
  var header = document.querySelector('.site-header');

  // Mobile nav
  var closeNav = function () {
    nav.classList.remove('open');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  };
  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    toggle.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeNav); });

  // In-page navigation. An anchor to a sticky header does nothing on iOS Safari, and with
  // mandatory scroll-snap on, browsers may yank a programmatic scroll back to the previously
  // snapped panel — so pause snapping, scroll, and restore it a beat after the scroll settles.
  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var restoreTimer = null;
  var scheduleRestore = function (ms) {
    clearTimeout(restoreTimer);
    restoreTimer = setTimeout(function () { root.style.scrollSnapType = ''; }, ms);
  };
  window.addEventListener('scrollend', function () { if (root.style.scrollSnapType === 'none') scheduleRestore(300); });
  var animateTo = function (target) {
    root.style.scrollSnapType = 'none';
    scheduleRestore(1800);                      // fallback for browsers without scrollend
    window.scrollTo({ top: target, behavior: reduceMotion ? 'auto' : 'smooth' });
  };
  var goTo = function (id) {
    if (!id || id === 'top') { animateTo(0); return; }
    var el = document.getElementById(id);
    if (el) animateTo(el.offsetTop - header.offsetHeight);
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="#"], button[data-top]');
    if (!a) return;
    e.preventDefault();
    closeNav();
    var id = a.hasAttribute('data-top') ? 'top' : a.getAttribute('href').slice(1);
    goTo(id);
    if (history.replaceState) history.replaceState(null, '', id === 'top' ? location.pathname : '#' + id);
  });
  var toTop = document.getElementById('toTop');

  // Compact header + back-to-top visibility
  var onScroll = function () {
    var y = window.scrollY;
    header.classList.toggle('scrolled', y > 12);
    toTop.classList.toggle('show', y > window.innerHeight * 0.8);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Active section in nav (scrollspy) + hide the mobile sticky CTA on the contact panel.
  // Pick the panel whose top is nearest the header line — deterministic on every scroll.
  var links = Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]:not(.nav__cta)'));
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
  var panels = Array.prototype.slice.call(document.querySelectorAll('.panel[id]'));
  var spyTick = false;
  var spy = function () {
    spyTick = false;
    var line = window.scrollY + header.offsetHeight + 8;
    var current = panels[0];
    panels.forEach(function (p) { if (p.offsetTop <= line) current = p; });
    links.forEach(function (a) { a.classList.toggle('active', byId[current.id] === a); });
    document.body.classList.toggle('on-contact', current.id === 'contact');
    document.body.classList.toggle('on-home', current.id === 'home');
  };
  window.addEventListener('scroll', function () { if (!spyTick) { spyTick = true; requestAnimationFrame(spy); } }, { passive: true });
  spy();

  if ('IntersectionObserver' in window) {
    // Reveal cards as they scroll into view
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.05 });
    document.querySelectorAll('[data-reveal]').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('[data-reveal]').forEach(function (el) { el.classList.add('in'); });
  }

  // Contact form: posts to a form service if data-endpoint is set,
  // otherwise opens the visitor's email app with the message filled in.
  var form = document.getElementById('contactForm');
  if (form) {
    var status = document.getElementById('cfStatus');
    var submit = form.querySelector('.cf-submit');
    var setStatus = function (msg, cls) { status.textContent = msg; status.className = 'cf-status ' + (cls || ''); };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = null;
      form.querySelectorAll('[required]').forEach(function (el) {
        var ok = el.checkValidity() && el.value.trim() !== '';
        el.classList.toggle('invalid', !ok);
        if (!ok && !bad) bad = el;
      });
      if (bad) { setStatus('Please fill in your name, a valid email and a message.', 'err'); bad.focus(); return; }
      if (form.botcheck.checked) { form.reset(); setStatus('Thanks! Your message was sent.', 'ok'); return; } // bot filled the hidden field: pretend success, send nothing

      var data = new FormData(form);
      var endpoint = form.getAttribute('data-endpoint');

      if (!endpoint) {
        var body = 'Name: ' + data.get('name') + '\nEmail: ' + data.get('email') +
          '\nOrganization: ' + (data.get('organization') || '-') + '\nTopic: ' + data.get('topic') +
          '\n\n' + data.get('message');
        window.location.href = 'mailto:' + form.getAttribute('data-mailto') +
          '?subject=' + encodeURIComponent('Website enquiry: ' + data.get('topic')) +
          '&body=' + encodeURIComponent(body);
        setStatus('Opening your email app…', 'ok');
        return;
      }

      submit.disabled = true;
      setStatus('Sending…');
      fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (res) { return res.json().catch(function () { return {}; }).then(function (j) { return { ok: res.ok && j.success !== false, j: j }; }); })
        .then(function (r) {
          if (!r.ok) throw new Error(r.j.message || 'send failed');
          form.reset();
          setStatus('Thanks! Your message was sent. We\'ll get back to you soon.', 'ok');
        })
        .catch(function () {
          setStatus('Sorry, something went wrong. Please email us at ' + form.getAttribute('data-mailto') + '.', 'err');
        })
        .then(function () { submit.disabled = false; });
    });

    form.addEventListener('input', function (e) { e.target.classList.remove('invalid'); });
  }

  // Hero slider: three slides, auto-advancing; pauses on hover, focus, the pause button, or when off screen
  var slidesWrap = document.getElementById('heroSlides');
  if (slidesWrap) {
    var slides = Array.prototype.slice.call(slidesWrap.children);
    var heroNav = document.getElementById('heroNav');
    var dots = Array.prototype.slice.call(heroNav.querySelectorAll('.hero__dots button'));
    var pauseBtn = document.getElementById('heroPause');
    var cur = 0, timer = null, userPaused = reduceMotion, hovering = false;
    var show = function (n) {
      cur = (n + slides.length) % slides.length;
      slides.forEach(function (sl, i) { sl.classList.toggle('is-active', i === cur); sl.setAttribute('aria-hidden', i === cur ? 'false' : 'true'); });
      dots.forEach(function (d, i) { d.setAttribute('aria-selected', i === cur ? 'true' : 'false'); });
    };
    var tick = function () {
      clearTimeout(timer);
      timer = setTimeout(function () {
        if (!userPaused && !hovering && !document.hidden && window.scrollY < window.innerHeight * 0.5) show(cur + 1);
        tick();
      }, 7000);
    };
    var setPaused = function (p) { userPaused = p; pauseBtn.classList.toggle('is-paused', p); pauseBtn.setAttribute('aria-label', p ? 'Play slides' : 'Pause slides'); };
    heroNav.hidden = false;
    setPaused(userPaused);
    heroNav.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b === pauseBtn) { setPaused(!userPaused); tick(); return; }
      var to = b.getAttribute('data-slide');
      show(to === 'prev' ? cur - 1 : to === 'next' ? cur + 1 : +to);
      tick();
    });
    var hero = document.getElementById('home');
    hero.addEventListener('mouseenter', function () { hovering = true; });
    hero.addEventListener('mouseleave', function () { hovering = false; });
    hero.addEventListener('focusin', function () { hovering = true; });
    hero.addEventListener('focusout', function () { hovering = false; });
    var x0 = null;
    slidesWrap.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    slidesWrap.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) { show(cur + (dx < 0 ? 1 : -1)); tick(); }
    }, { passive: true });
    show(0);
    tick();
  }

  // Auto year in footer
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
