---
layout: page
title: Upcoming Events
permalink: /upcoming-events/
---

Welcome to our events page.

To register directly from our website, click on the relevant link below. You'll need to have a Neon account to register.

Please check your inbox (and sometimes your spam folder) for event-specific emails and our weekly newsletter, *This Week at MNS*, which is sent every Sunday.

For any questions, please reach out to [info@mnspta.org](mailto:info@mnspta.org).

{% if site.data.events and site.data.events.size > 0 %}
  {% for event in site.data.events %}
  <div class="event-card">
    {% if event.image %}<img src="{{ event.image | relative_url }}" alt="{{ event.title }}">{% endif %}
    <div>
      <h3>{{ event.title }}</h3>
      <p class="event-meta">{{ event.date }}{% if event.price %} · {{ event.price }}{% endif %}</p>
      {% if event.description %}<p>{{ event.description }}</p>{% endif %}
      {% if event.register_url %}<a class="btn btn--primary" href="{{ event.register_url }}">Register</a>{% endif %}
    </div>
  </div>
  {% endfor %}
{% else %}
  <div class="callout">
    <p>No upcoming events posted at the moment. Check back soon, or watch <em>This Week at MNS</em> for the latest.</p>
  </div>
{% endif %}
