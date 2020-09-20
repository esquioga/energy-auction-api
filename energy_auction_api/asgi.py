"""App entrypoint"""
from os import environ

from .app_factory import create_app

app = create_app(environ)
