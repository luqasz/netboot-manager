import os

import sentry_sdk
from sentry_sdk.integrations.pyramid import PyramidIntegration


def init():
    sentry_sdk.init(
        dsn=os.environ.get('SENTRY_DSN', ''),
        integrations=[PyramidIntegration()]
    )
