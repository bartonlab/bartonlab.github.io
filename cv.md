---
layout: cv
---

<!-- PUBLICATIONS -->

<div class="grid">
    <div class="column-left">
        <div class="content-left">
            <h2>Publications</h2>
        </div>
    </div>
    <div class="column-right">
        <hr />
    </div>
</div>

<div class="grid">
    <div class="column-right">
        <div class="content-right">
            <sup>=</sup> equal contributions, <sup>c</sup> co-corresponding authors
        </div>
    </div>
{% assign last_year = 9999 %}
{% for paper in site.data.publications %}
    {% if paper.preprint != true %}
        {% if paper.year != last_year %}
            <div class="column-left-top">
                <div class="content-left">
                    {{ paper.year }}
                </div>
            </div>
            {% assign last_year = paper.year %}
        {% endif %}
        <div class="column-right">
            <div class="content-right">
                <b>{{ paper.title }}</b>
                <br>
                {{ paper.authors }}
                <br>
                {{ paper.journal }}
                {% if paper.volume != 'NA' %}
                    {% if paper.number != 'NA' %}
                        {% if paper.pages != 'NA' %}
                            {{ paper.volume }} ({{ paper.number }}): {{ paper.pages }}
                        {% else %}
                            {{ paper.volume }} ({{ paper.number }})
                        {% endif %}
                    {% elsif paper.pages != 'NA' %}
                        {{ paper.volume }}: {{ paper.pages }}
                    {% endif %}
                {% elsif paper.pages != 'NA' %}
                    {{ paper.pages }}
                {% endif %}
            </div>
        </div>
    {% endif %}
{% endfor %}
</div>

<!-- TALKS AND PRESENTATIONS -->

<div class="grid">
    <div class="column-left">
        <div class="content-left">
            <h2>Invited Talks</h2>
        </div>
    </div>
    <div class="column-right">
        <hr />
    </div>
</div>

<div class="grid">
{% assign last_year = 9999 %}
{% for talk in site.data.talks %}
    {% if talk.invited == true %}
        {% if talk.year != last_year %}
            <div class="column-left-top">
                <div class="content-left">
                    {{ talk.year }}
                </div>
            </div>
            {% assign last_year = talk.year %}
        {% endif %}
        <div class="column-right">
            <div class="content-right">
                {{ talk.title }}
            </div>
        </div>
    {% endif %}
{% endfor %}
</div>

<div class="grid">
    <div class="column-left">
        <div class="content-left">
            <h2>Contributed Presentations</h2>
        </div>
    </div>
    <div class="column-right">
        <hr />
    </div>
</div>

<div class="grid">
{% assign last_year = 9999 %}
{% for talk in site.data.talks %}
    {% if talk.invited != true %}
        {% if talk.year != last_year %}
            <div class="column-left-top">
                <div class="content-left">
                    {{ talk.year }}
                </div>
            </div>
            {% assign last_year = talk.year %}
        {% endif %}
        <div class="column-right">
            <div class="content-right">
                {{ talk.title }}
            </div>
        </div>
    {% endif %}
{% endfor %}
</div>


<!-- HONORS & AWARDS -->

<div class="grid">
    <div class="column-left">
        <div class="content-left">
            <h2>Honors & Awards</h2>
        </div>
    </div>
    <div class="column-right">
        <hr />
    </div>
</div>

<div class="grid">
{% for award in site.data.awards %}
    {% if award.selected == true %}
        <div class="column-right">
            <div class="content-right">
                {{ award.title }}
                {% if award.years %}
                    ({{ award.years }})
                {% endif %}
            </div>
        </div>
    {% endif %}
{% endfor %}
</div>

<!-- TEACHING EXPERIENCE -->

<div class="grid">
    <div class="column-left">
        <div class="content-left">
            <h2>Teaching Experience & Certification</h2>
        </div>
    </div>
    <div class="column-right">
        <hr />
    </div>
</div>

<div class="grid">
    <div class="column-right">
        <div class="content-right">
            Completed MIT Kaufman Teaching Certificate Program (2017)
        </div>
    </div>
{% for class in site.data.classes %}
    <div class="column-right">
        <div class="content-right">
            {% if class.TA == true %}
                Teaching assistant:
            {% endif %}
            {{ class.title }}
            {% if class.years %}
                ({{ class.years }})
            {% endif %}
        </div>
    </div>
{% endfor %}
</div>
