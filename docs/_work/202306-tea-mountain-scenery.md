---
layout: work

title: Tea Mountain Scenery
work_dir: 202306-tea-mountain-scenery
thumb_name: tea-mountain-scenery-1.jpg

works:
  - tea-mountain-scenery-1.jpg
  - tea-mountain-scenery-2.jpg
  - tea-mountain-scenery-3.jpg
  - tea-mountain-scenery-4.jpg
  - tea-mountain-scenery-5.jpg
---

<div class="grid row">
    {% for w in page.works %}
    <div class="col-6 col-md-6">
        <img src="{{ site.personal_work_dir }}/{{ page.work_dir }}/{{ w }}" data-fancybox="gallery" class="img-fluid" alt="Image 1">
    </div>
    {% endfor %}
<div>
