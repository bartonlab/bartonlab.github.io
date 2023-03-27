---
layout: page
title: Code
---

<div class="smallspacer"></div>

<ul class="code-list">
{% for project in site.data.projects %}
    <li>
        <a class="project-title" href="{{ project.url }}">{{ project.title }}</a>
        <div class="smallspacer"></div>
        <a class="project-subtitle" href="{{ project.url }}">{{ project.description }}</a>
        <div class="smallspacer"></div>
        <small>
	        Updated
	        <a href="{{ project.commits.first.url }}">
	            {{ project.commits.first.date | date: "%-d %b %Y" }}
	        </a>
	        by
	        <a href="{{ project.commits.first.author_url }}">				
                {{ project.commits.first.author_login }}
	        </a>
        </small>
	    <div class="bigspacer"></div>
        <div class="spacer"></div>
    </li>
{% endfor %}
</ul>
