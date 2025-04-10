---
layout: work

title: Tiny World
work_dir: 202305-tiny-world
thumb_name: tiny-world-1.jpg

works:
  - tiny-world-1.jpg
  - tiny-world-2.jpg
  - tiny-world-3.jpg
  - tiny-world-4.jpg
---

<div class="grid row">
    {% for w in page.works %}
    <div class="col-6 col-md-6">
        <img src="{{ site.personal_work_dir }}/{{ page.work_dir }}/{{ w }}" data-fancybox="gallery" class="img-fluid" alt="Image 1">
    </div>
    {% endfor %}
<div>
