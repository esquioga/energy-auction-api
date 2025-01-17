"""Module exposing auction router"""
from enum import Enum

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


@ROUTER.get('/power-sources')
def get_power_sources(auction_controller: AuctionController = get_controller(
    'AuctionController')):
    return auction_controller.get_unique_power_source()


@ROUTER.get('/detail')
def get_seller_details(text: str,
                       query_type: int,
                       auction_controller: AuctionController = get_controller(
                           'AuctionController')):
    return auction_controller.get_company_detail(text, query_type)
