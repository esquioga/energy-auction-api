"""Module exposing application factory"""
from fastapi import FastAPI
from pymongo import MongoClient

from .controllers.auction import AuctionController
from .utils.controller_registry import register_controller
from .routes.auction import ROUTER as auction_router


def create_app(conf):
    """App factory creation function"""
    app = FastAPI()

    mongodb_client = MongoClient(conf.get('MONGODB_URL'))
    database = mongodb_client[conf['MONGODB_DB']]
    auction_collection = database[conf['MONGODB_COLLECTION']]

    auction_controller = AuctionController(
        auction_collection=auction_collection)
    register_controller(app, auction_controller)

    app.include_router(auction_router)

    return app
