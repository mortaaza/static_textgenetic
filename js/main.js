// TextGenetic AI — lightweight interactions (no dependencies)
(function () {
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

  // Back-to-top button visibility
  var toTop = document.querySelector('.to-top');
  window.addEventListener('scroll', function () {
    if (window.scrollY > 480) toTop.classList.add('show');
    else toTop.classList.remove('show');
  });

  // Auto year in footer
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
