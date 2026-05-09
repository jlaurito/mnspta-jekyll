---
layout: page
title: Our Executive Board and Parent Leaders
permalink: /executive-board/
---

{%- comment -%}
This page renders entirely from _data/board.yml. To update for a new
school year, edit that file — do not edit this page.
{%- endcomment -%}

<section class="board-section">
  <h2>Executive Board for the {{ site.data.board.school_year }} School Year</h2>
  <dl class="role-list">
    {%- for entry in site.data.board.executive_board %}
    <div class="role">
      <dt>{{ entry.role }}</dt>
      <dd>
        {%- if entry.members -%}
          {%- for m in entry.members -%}
            {{ m }}{%- unless forloop.last %}<br>{% endunless -%}
          {%- endfor -%}
        {%- endif -%}
        {%- if entry.email %}<span class="role__email">{{ entry.email }} [at] mnspta [dot] org</span>{%- endif -%}
      </dd>
    </div>
    {%- endfor %}
  </dl>
</section>

<section class="board-section">
  <h2>Parent Leaders</h2>
  <dl class="role-list">
    {%- for entry in site.data.board.parent_leaders %}
    <div class="role">
      <dt>{{ entry.role }}</dt>
      <dd>
        {%- if entry.members -%}
          {%- for m in entry.members -%}
            {{ m }}{%- unless forloop.last %}<br>{% endunless -%}
          {%- endfor -%}
        {%- endif -%}
        {%- if entry.sub_roles -%}
          {%- for sub in entry.sub_roles -%}
            {{ sub.name }}<span class="role__email">{{ sub.email }} [at] mnspta [dot] org</span>{%- unless forloop.last %}<br>{% endunless -%}
          {%- endfor -%}
        {%- elsif entry.email -%}
          <span class="role__email">{{ entry.email }} [at] mnspta [dot] org</span>
        {%- endif -%}
      </dd>
    </div>
    {%- endfor %}
  </dl>
</section>
