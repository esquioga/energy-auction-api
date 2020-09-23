"""Utility module to manage registry and injection of controllers."""
from fastapi import Depends, FastAPI
from starlette.requests import Request


def register_controller(app: FastAPI, controller):
    """Register a controller to be injected in the future"""
    async def inject_controller(request: Request, call_next):
        setattr(request.state, controller.__class__.__name__, controller)
        return await call_next(request)

    app.middleware('http')(inject_controller)


def get_controller(class_name):
    """Generate a dependency to inject controllers in the request."""
    def getter(request: Request):
        return getattr(request.state, class_name)

    return Depends(getter)
