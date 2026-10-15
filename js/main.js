// TextGenetic AI — lightweight interactions (no dependencies)
(function () {
  document.documentElement.classList.add('js');
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('nav');

  // Mobile nav
  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    toggle.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Close mobile nav after clicking a link
  nav.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () {
      nav.classList.remove('open');
      toggle.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });

  // Back-to-top button + compact header on scroll
  var toTop = document.querySelector('.to-top');
  var header = document.querySelector('.site-header');
  var onScroll = function () {
    toTop.classList.toggle('show', window.scrollY > 480);
    header.classList.toggle('scrolled', window.scrollY > 12);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Reveal sections/cards as they scroll into view
  var revealEls = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
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

  // Auto year in footer
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
