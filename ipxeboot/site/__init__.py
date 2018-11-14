from pyramid.view import view_config


@view_config(
    route_name='root',
    request_method='GET',
    renderer='templates/main.jinja2',
)
def main_page(request):
    return {}
