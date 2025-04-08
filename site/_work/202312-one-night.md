---
layout: work

title: One Night
work_dir: 202312-one-night
thumb_name: one-night-1.jpg

works:
  - one-night-1.jpg
  - one-night-2.jpg
  - one-night-4.jpg
  - one-night-5.jpg
  - one-night-6.jpg
---

<div class="grid row">
    {% for w in page.works %}
    <div class="col-6 col-md-6 grid-item2 grid-sizer">
        <img src="{{ site.personal_work_dir }}/{{ page.work_dir }}/{{ w }}" data-fancybox="gallery" class="img-fluid" alt="Image 1">
    </div>
    {% endfor %}
<div>
