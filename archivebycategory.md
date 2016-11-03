---
layout: page
title: Post by Category
permalink: /categoryview/
sitemap: false
---

<!--
Section 3: Category List
After the front matter, add the following code to display the categories and the number of posts per category. Each category will link to further down in the page where is will show the post for that category.
Display categories and number of posts.
-->

<div>
{% assign categories = site.categories | sort %}
{% for category in categories %}
 <span class="site-tag">
    <a href="#{{ category | first | slugify }}">
            {{ category[0] | replace:'-', ' ' }} ({{ category | last | size }})
    </a>
</span>
{% endfor %}
</div>


<!--
Section 4: Blog Post by Category
Next you need to add the code to display the list of blog post by category and sorted by title}
-->

<div id="index">

{% for category in categories %}
<a name="{{ category[0] }}"></a><h2>{{ category[0] | replace:'-', ' ' }} ({{ category | last | size }}) </h2>
{% assign sorted_posts = site.posts | sort: 'title' %}
{% for post in sorted_posts %}
{%if post.categories contains category[0]%}

  <h3><a href="{{ site.url }}{{site.baseurl}}{{ post.url }}" title="{{ post.title }}">{{ post.title }} <p class="date">{{ post.date |  date: "%B %e, %Y" }}</p></a></h3>
   <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>

{%endif%}
{% endfor %}

{% endfor %}
</div>
