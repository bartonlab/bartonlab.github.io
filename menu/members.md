---
layout: page
title: Members
---

<br>

{% for member in site.data.members %}
{% if member.alumni != true %}
<div class="grid">
  <div class="member-left">
		{% if member.image %}
			<img class="theme" src="{{ site.github.url }}/{{ member.image }}" width="120">
		{% endif %}
    <p style="margin-bottom:0px; margin-top:10px;">
      {% if member.cv %}
        <small><a href="{{ site.github.url }}/{{ member.cv }}">CV</a></small>
      {% endif %}		
      {% if member.twitter %}
        <a href="https://twitter.com/{{ member.twitter }}" target="_blank"><i class="fa fa-twitter" aria-hidden="true"></i></a>		
      {% endif %}
      {% if member.github %}
        <a href="https://github.com/{{ member.github }}" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>
      {% endif %}		
      {% if member.scholar %}
        <a href="https://scholar.google.com/citations?user={{ member.scholar }}" target="_blank"><i class="fa fa-book" aria-hidden="true"></i></a>
      {% endif %}				   	
      {% if member.email %}
        <a href="mailto:{{ member.email }}"><i class="fa fa-envelope" aria-hidden="true" style="padding: 5px;"></i></a>
      {% endif %}				   	
      {% if member.powur %}
        <a href="https://sites.google.com/view/ucr-powur/" target="_blank"><i class="fa fa-bolt" aria-hidden="true"></i></a>
      {% endif %}
    </p>
	</div>
  <div class="member-right">
    {{ member.blurb }}
  </div>
  <p style="margin-bottom:0px; margin-top:0px;"></p>
</div>
{% endif %}
{% endfor %}
