from ipxeboot.vars import IPXE_HEADER_REGEXP


def includeme(config):
    config.add_static_view(
        'static',
        'static',
        cache_max_age=3600
    )
    config.add_route(
        name='root',
        pattern='',
        request_method=('GET', 'POST'),
    )
    config.add_route(
        name='os_name_version',
        pattern='/{name}/{version}',
        request_method='GET',
        header=IPXE_HEADER_REGEXP,
    )
