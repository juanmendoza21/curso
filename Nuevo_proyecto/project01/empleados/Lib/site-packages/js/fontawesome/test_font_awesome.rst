How to use?
===========

This package supports two flavours of Font Awesome:

SVG with JS
-----------

You can import ``fontawesome_js`` from ``js.fontawesome`` and ``need`` it
where you want these resources to be included on a page::

  >>> from js.fontawesome import fontawesome_js
  >>> fontawesome_js.need()

There are also resources for the icon subsets provided by Font Awesome:

* fa_brands_js
* fa_regular_js
* fa_solid_js

``fa_v4_shims_js`` provides the BBB shim for version 4 of Font Awesome.


Web Fonts with CSS
------------------

You can import ``fontawesome_all_css`` from ``js.fontawesome`` and ``need`` it
where you want these resources to be included on a page::

  >>> from js.fontawesome import fontawesome_all_css
  >>> fontawesome_all_css.need()

There are also resources for the icon subsets provided by Font Awesome:

* fa_brands_css
* fa_regular_css
* fa_solid_css
