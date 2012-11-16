from fanstatic import Library, Resource, Group
from js.d3 import d3

library = Library('rickshaw', 'resources')
rickshaw_css = Resource(library, 'rickshaw.css', minified='rickshaw.min.css')
rickshaw_js = Resource(library, 'rickshaw.js', minified='rickshaw.min.js', depends=[d3])
rickshaw = Group([rickshaw_css, rickshaw_js])
