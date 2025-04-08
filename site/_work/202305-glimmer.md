---
layout: work

title: Glimmer
work_dir: 202301-glimmer
thumb_name: glimmer-1.jpg

works:
  - glimmer-1.jpg
  - glimmer-2.jpg
  - glimmer-3.jpg
  - glimmer-4.jpg
  - glimmer-5.jpg
  - glimmer-6.jpg
  - glimmer-7.jpg
  - glimmer-8.jpg
  - glimmer-9.jpg
---

<div class="grid row">
    {% for w in page.works %}
    <div class="col-6 col-md-6 grid-item2 grid-sizer">
        <img src="{{ site.personal_work_dir }}/{{ page.work_dir }}/{{ w }}" data-fancybox="gallery" class="img-fluid" alt="Image 1">
    </div>
    {% endfor %}
<div>
