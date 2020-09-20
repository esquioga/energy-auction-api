"""Module exposing application factory"""
from fastapi import FastAPI

def create_app(conf):
    """App factory creation function"""
    app = FastAPI()

    return app
