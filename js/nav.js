// Shared header menu: the Projects dropdown on every page, and the phone menu on sub-pages.
(function () {
  var nav = document.getElementById('nav'), toggle = document.getElementById('navToggle');
  if (!nav) return;
  // Sub-pages do not load main.js, so the phone menu button is wired here
  if (toggle && !window.TG_MAIN) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  var groups = nav.querySelectorAll('.nav__group');
  var closeAll = function (except) {
    groups.forEach(function (g) { if (g !== except) { g.classList.remove('is-open'); g.querySelector('.nav__drop').setAttribute('aria-expanded', 'false'); } });
  };
  groups.forEach(function (g) {
    var btn = g.querySelector('.nav__drop');
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = !g.classList.contains('is-open');
      closeAll(g);
      g.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.nav__group')) closeAll(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });
  // Mark the current page in the menu
  var here = location.pathname.replace(/index\.html$/, '');
  nav.querySelectorAll('a[href^="/"]').forEach(function (a) {
    if (a.getAttribute('href') === here && here !== '/') a.classList.add('active');
  });
})();
