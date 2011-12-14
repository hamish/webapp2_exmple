import webapp2
from handlers import DebugHandler, IndexHandler
   
config = {}
config['webapp2_extras.jinja2'] = {
    'template_path': 'templates',
    'compiled_path': None,
    'force_compiled': False,
    'environment_args': {
        'autoescape': True,
        'extensions': [
            'jinja2.ext.autoescape',
            'jinja2.ext.with_'
            ]
        },
    'globals': {
        'url_for' : webapp2.uri_for
        },
    'filters': None,
    }

application = webapp2.WSGIApplication([
        webapp2.Route(r'/', handler=IndexHandler, name='index'),
        webapp2.Route(r'/debug/', handler=DebugHandler, name='debug'),
        ], debug=True, config=config)

