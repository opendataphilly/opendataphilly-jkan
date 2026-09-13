Homepage hero images
=====================

The images in this folder are shown in the rotating hero banner at the top of
the homepage. The slideshow crossfades between them every 6 seconds and only
rotates when two or more images are configured.

Image guidance
--------------
- Orientation: landscape (wide). The banner is full width and fairly short.
- Recommended size: at least 1600 x 700 px. Wider is fine.
- The image is displayed with `background-size: cover`, so it is cropped to
  fill the banner and centered (`background-position: center`). Keep the most
  important content near the middle so it is not cropped out.
- Format: PNG or JPG, optimized for the web. Aim for under ~300 KB per image
  so the homepage stays fast.
- The left third of the banner sits under a dark gradient with the site
  greeting on top, so avoid putting critical detail in that area.

How to add a new hero image
----------------------------
1. Add the image file to this folder (/img/hero-images/).
2. Open _config.yml at the repository root and add an entry under
   `hero_images` with:
       image  - path to the file, e.g. /img/hero-images/hero-image-example.png
       alt    - a short description of the image, for screen readers (required)
       url    - link to the related dataset in the catalog (optional). When
                set, a "View related dataset" link appears over the image so
                visitors can find the data the image came from. Leave it blank
                for no link.

To remove an image from the slideshow, delete its entry from `hero_images` in
_config.yml (and delete the file here if it is no longer used).
