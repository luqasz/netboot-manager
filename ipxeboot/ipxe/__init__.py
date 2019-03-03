import logging
from urllib.parse import urljoin
from posixpath import join

import jinja2

from ipxeboot.vars import (
    IPXE_HEADER_REGEXP,
    IPXE_SCRIPT_HEADER,
    IPXE_HTTP_VARS,
)
from pyramid.response import (
    Response,
    response_adapter,
)
from pyramid.view import view_config

log = logging.getLogger(__name__)


class IpxeOptions:

    env = jinja2.Environment(
        trim_blocks=False,
        lstrip_blocks=False,
        newline_sequence='\n',
        keep_trailing_newline=True,
        loader=jinja2.FileSystemLoader(searchpath='ipxeboot/ipxe/templates/'),
        undefined=jinja2.StrictUndefined,
    )

    def __init__(self, name, params):
        """
        :param name: Name of ipxe template.
        :param params: Parameters for template rendering.
        """
        self.name = name
        self.params = params

    def __str__(self):
        template = self.env.get_template(self.name + '.jinja2')
        rendered = template.render(self.params).strip()
        script = (IPXE_SCRIPT_HEADER, rendered)
        return '\n'.join(script)

    def __bytes__(self):
        return str(self).encode(encoding='utf-8')


@response_adapter(IpxeOptions)
def boot_options_adapter(obj):
    response = Response(bytes(obj))
    response.content_type = 'text/plain'
    return response


@view_config(
    route_name='root',
    request_method='GET',
    header=IPXE_HEADER_REGEXP,
)
def main_menu_get(request):
    return IpxeOptions(
        name='main_get',
        params=dict(
            base_url=request.host_url,
            variables=IPXE_HTTP_VARS,
        ),
    )


@view_config(
    route_name='root',
    request_method='POST',
    header=IPXE_HEADER_REGEXP,
)
def main_menu_post(request):
    return IpxeOptions(
        name='main_post',
        params=dict(
            base_url=request.host_url,
        ),
    )


@view_config(
    route_name='os_name_version',
)
def os_name_version(request):
    log.debug("matchdict %s", request.matchdict)
    log.debug("params %s", request.params)
    return IpxeOptions(
        name=join('linux', request.matchdict['name']),
        params={
            'version': request.matchdict['version'],
        },
    )
