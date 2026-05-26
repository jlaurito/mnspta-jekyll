---
layout: home
title: Home
description: The MNS PTA supports the school community of PS290 Manhattan New School.
permalink: /
---

<section class="hero">
  {%- assign slides = site.hero.slides -%}
  <div class="hero__slideshow{% if slides.size > 1 %} is-slideshow{% endif %}"
       data-interval="{{ site.hero.interval | default: 5 }}"
       role="region" aria-roledescription="carousel" aria-label="Photos of the MNS community">
    {%- for slide in slides %}
    <div class="hero__slide{% if forloop.first %} is-active{% endif %}"
         {% unless forloop.first %}aria-hidden="true"{% endunless %}>
      <img src="{{ slide.image | relative_url }}" alt="{{ slide.alt }}"
           {% unless forloop.first %}loading="lazy"{% endunless %}>
    </div>
    {%- endfor %}

    {%- if slides.size > 1 %}
    <div class="hero__dots" role="tablist" aria-label="Choose slide">
      {%- for slide in slides %}
      <button class="hero__dot{% if forloop.first %} is-active{% endif %}"
              type="button" role="tab"
              aria-label="Slide {{ forloop.index }}"
              aria-selected="{% if forloop.first %}true{% else %}false{% endif %}"></button>
      {%- endfor %}
    </div>
    {%- endif %}
  </div>
  <div class="hero__statement">
    <p>The Manhattan New School Parent-Teacher Association supports the school community, working together to help our children grow into confident, enthusiastic life-long learners.</p>
  </div>
</section>

<section class="tile-grid">
  <div class="tile">
    <img src="{{ '/assets/images/volunteer-flyer.jpg' | relative_url }}" alt="Volunteer with the PTA">
    <h3>All MNS families are PTA members</h3>
    <p>Even a few hours of your time can make an enormous difference and help organize programs and events for our community. It really does take a village!</p>
    <a class="tile__cta" href="{{ '/and-more/' | relative_url }}">See how you can help →</a>
  </div>

  <div class="tile">
    <img src="{{ '/assets/images/annual-appeal-icon.png' | relative_url }}" alt="Annual Appeal">
    <h3>Annual Appeal</h3>
    <p>Our PTA covers many expenses that allow the school to function at a basic level while also making MNS exceptional. Find out which services and programs are funded by the PTA — and how you can help.</p>
    <a class="tile__cta" href="{{ '/annual-appeal/' | relative_url }}">Learn more →</a>
  </div>

  <div class="tile">
    <img src="{{ '/assets/images/mables-logo.png' | relative_url }}" alt="Mabel's Labels">
    <img src="{{ '/assets/images/minted-logo.png' | relative_url }}" alt="Minted">
    <h3>Shopping Rewards</h3>
    <p>The MNS PTA has set up rewards programs that give back to the school every time you shop on Minted and Mabel's Labels.</p>
    <a class="tile__cta" href="{{ '/shopping-rewards/' | relative_url }}">Shop &amp; give back →</a>
  </div>
</section>

<div class="section-divider"><hr></div>

<section class="tile-grid">
  <div class="tile">
    <img src="{{ '/assets/images/school-store.png' | relative_url }}" alt="MNS School Spirit Store">
    <h3>School Store</h3>
    <p>Take a look at the full catalog of MNS school spirit items.</p>
    <a class="tile__cta" href="{{ site.external.spirit_store_url }}">Visit the store →</a>
  </div>

  <div class="tile">
    <img src="{{ '/assets/images/mns-bulletin.png' | relative_url }}" alt="MNS Bulletin">
    <h3>Welcome from your PTA presidents</h3>
    <p>Read this year's welcome email — what to expect, who to contact, and how to plug in.</p>
    <a class="tile__cta" href="{{ site.external.welcome_email }}">Read the welcome →</a>
  </div>
</section>

<section class="quick-links">
  <h2>Quick links</h2>
  <ul>
    <li><a href="{{ '/calendar-subscribe/' | relative_url }}">Sync the MNS PTA calendar to your device</a></li>
    <li><a href="{{ site.external.expense_reimbursement_form }}">Submit an expense reimbursement report</a></li>
    <li><a href="{{ site.external.unpaid_invoices_form }}">Submit unpaid invoices for payment</a></li>
  </ul>
</section>
<script>
  (function () {
    var shows = document.querySelectorAll('.hero__slideshow.is-slideshow');
    shows.forEach(function (show) {
      var slides = Array.prototype.slice.call(show.querySelectorAll('.hero__slide'));
      var dots = Array.prototype.slice.call(show.querySelectorAll('.hero__dot'));
      if (slides.length < 2) return;

      var interval = (parseFloat(show.getAttribute('data-interval')) || 5) * 1000;
      var current = 0;
      var timer = null;
      var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      function show_slide(next) {
        next = (next + slides.length) % slides.length;
        slides[current].classList.remove('is-active');
        slides[current].setAttribute('aria-hidden', 'true');
        slides[next].classList.add('is-active');
        slides[next].removeAttribute('aria-hidden');
        if (dots.length) {
          dots[current].classList.remove('is-active');
          dots[current].setAttribute('aria-selected', 'false');
          dots[next].classList.add('is-active');
          dots[next].setAttribute('aria-selected', 'true');
        }
        current = next;
      }

      function start() {
        if (reduce || timer) return;
        timer = setInterval(function () { show_slide(current + 1); }, interval);
      }
      function stop() {
        if (timer) { clearInterval(timer); timer = null; }
      }

      dots.forEach(function (dot, i) {
        dot.addEventListener('click', function () {
          stop();
          show_slide(i);
          start();
        });
      });

      // Pause on hover / focus so people can read
      show.addEventListener('mouseenter', stop);
      show.addEventListener('mouseleave', start);
      show.addEventListener('focusin', stop);
      show.addEventListener('focusout', start);

      // Pause when the tab is hidden
      document.addEventListener('visibilitychange', function () {
        if (document.hidden) { stop(); } else { start(); }
      });

      start();
    });
  })();
</script>
