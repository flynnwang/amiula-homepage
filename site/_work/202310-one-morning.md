---
layout: work

title: One Morning
work_dir: 202310-one-morning
thumb_name: one-morning-1.jpg

works:
  - one-morning-1.jpg
  - one-morning-2.jpg
  - one-morning-3.jpg
  - one-morning-4.jpg
  - one-morning-5.jpg
---

<div class="grid row">
    {% for w in page.works %}
    <div class="col-6 col-md-6">
        <img src="{{ site.personal_work_dir }}/{{ page.work_dir }}/{{ w }}" data-fancybox="gallery" class="img-fluid" alt="Image 1">
    </div>
    {% endfor %}
<div>
