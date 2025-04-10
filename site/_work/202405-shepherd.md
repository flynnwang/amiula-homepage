---
layout: work

title: Shepherd
work_dir: 202405-shepherd
thumb_name: img20240517_17412824.jpg

works:
  - img20240517_17412824.jpg
  - img20240517_17432233.jpg
---

<div class="grid row">
    {% for w in page.works %}
    <div class="col-6 col-md-6">
        <img src="{{ site.personal_work_dir }}/{{ page.work_dir }}/{{ w }}" data-fancybox="gallery" class="img-fluid" alt="Image 1">
    </div>
    {% endfor %}
<div>
