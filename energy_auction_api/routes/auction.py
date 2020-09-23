"""Module exposing auction router"""
from fastapi.routing import APIRouter

from ..utils.controller_registry import get_controller
from ..controllers.auction import AuctionController, CompanyType

ROUTER = APIRouter()


@ROUTER.get('/sellers')
def get_sellers(auction_controller: AuctionController = get_controller(
    'AuctionController')):
    """Returns sellers list"""
    return auction_controller.get_unique_companies(CompanyType.seller)


@ROUTER.get('/buyers')
def get_buyers(auction_controller: AuctionController = get_controller(
    'AuctionController')):
    """Returns buyers list"""
    return auction_controller.get_unique_companies(CompanyType.buyer)
