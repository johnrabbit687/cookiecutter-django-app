"""Pre-generation cookiecutter hook for validation of the app_name parameter."""

from __future__ import absolute_import, unicode_literals

import re
import sys

import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('pre_gen_project')  # pylint: disable=C0103

APP_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

APP_NAME = '{{cookiecutter.app_name}}'

if not re.match(APP_REGEX, APP_NAME):
    logger.error('Invalid value for app_name "{}"'.format(APP_NAME))
    sys.exit(1)
