from fanstatic import Library, Resource

library = Library('font_awesome', 'resources')

fontawesome_css = Resource(
    library,
    'css/fontawesome.css',
    minified='css/fontawesome.min.css')

fa_brands_css = Resource(
    library,
    'css/fa-brands.css',
    minified='css/fa-brands.min.css',
    depends=[fontawesome_css])

fa_regular_css = Resource(
    library,
    'css/fa-regular.css',
    minified='css/fa-regular.min.css',
    depends=[fontawesome_css])

fa_solid_css = Resource(
    library,
    'css/fa-solid.css',
    minified='css/fa-solid.min.css',
    depends=[fontawesome_css])

fa_svg_with_js_css = Resource(
    library,
    'css/fa-svg-with-js.css',
    minified='css/fa-svg-with-js.min.css')

fontawesome_all_css = Resource(
    library,
    'css/fontawesome-all.css',
    minified='css/fontawesome-all.min.css')

fontawesome_js = Resource(
    library,
    'js/fontawesome.js',
    minified='js/fontawesome.min.js')

fa_brands_js = Resource(
    library,
    'js/fa-brands.js',
    minified='js/fa-brands.min.js',
    depends=[fontawesome_js])

fa_regular_js = Resource(
    library,
    'js/fa-regular.js',
    minified='js/fa-regular.min.js',
    depends=[fontawesome_js])

fa_solid_js = Resource(
    library,
    'js/fa-solid.js',
    minified='js/fa-solid.min.js',
    depends=[fontawesome_js])

fa_v4_shims_js = Resource(
    library,
    'js/fa-v4-shims.js',
    minified='js/fa-v4-shims.min.js')

fontawesome_all_js = Resource(
    library,
    'js/fontawesome-all.js',
    minified='js/fontawesome-all.min.js')
