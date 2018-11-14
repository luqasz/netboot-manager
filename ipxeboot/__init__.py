from collections import ChainMap

from ipxeboot import routes, sentry
from ipxeboot.vars import IPXE_HEADER_REGEXP
from pyramid.config import Configurator

default_settings = {
    'jinja2.lstrip_blocks': 'true',
    'jinja2.trim_blocks': 'true',
    'pyramid.default_locale_name': 'en',
    'debugtoolbar.hosts': '127.0.0.1 ::1',
    'pyramid.debug_authorization': 'false',
    'pyramid.debug_notfound': 'false',
    'pyramid.debug_routematch': 'false',
    'pyramid.debug_all': 'false',
}


def main(**settings):
    config = Configurator(
        settings=ChainMap(
            settings,
            default_settings,
        )
    )
    config.include('pyramid_jinja2')
    config.include(routes)
    config.scan()
    return config.make_wsgi_app()


def waitress_app(global_config, **settings):
    return main(**settings)


def uwsgi_app(env, start_response):
    sentry.init()
    wsgi = main()
    return wsgi(env, start_response)
