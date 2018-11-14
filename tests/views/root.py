import pytest
from ipxeboot import main
from webtest import TestApp as WebTestApp


class Test_Root_IPXE_Agent:

    def setup(self):
        app = main()
        self.testapp = WebTestApp(app)

    def ipxeget(self, *args, **kwargs):
        return self.testapp.get(
            *args,
            headers={'User-Agent': 'iPXE/1.0.0'},
            **kwargs,
        )

    def test_get(self):
        self.ipxeget('/', status=200)

    def test_ipxe_script_response(self):
        resp = self.ipxeget('/', status=200)
        assert resp.body.startswith(b'#!ipxe')


class Test_Root_Non_IPXE_Agent:

    def setup(self):
        app = main()
        self.testapp = WebTestApp(app)

    @pytest.mark.parametrize("agent", (
        'Mozilla/5.0',
        'iPXE',
        'ipxe/version',
    ))
    def test_not_ipxe_script_response(self, agent):
        resp = self.testapp.get('/', status=200, headers={'User-Agent': agent})
        assert not resp.body.startswith(b'#!ipxe')
