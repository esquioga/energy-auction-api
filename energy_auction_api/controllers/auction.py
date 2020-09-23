"""Module exposing Auction controller"""
from logging import getLogger
from typing import List, Dict
from enum import Enum

from pymongo.collection import Collection

from ..adapters.auctions import parse_xsl

LOGGER = getLogger("uvicorn.error")


class CompanyType(Enum):
    """Enum for company type"""
    seller = 'seller'
    buyer = 'buyer'


class AuctionController:
    """Class to handle all auction operations"""
    def __init__(self, auction_collection: Collection):
        self._auction_collection = auction_collection

    def consume_auctions(self, file):
        """Saves energy auction data"""
        auction_data = parse_xsl(file)
        for auction in auction_data:
            self._auction_collection.update(
                {'auction_id': auction.get('auction_id')},
                auction,
                upsert=True)

    def get_unique_companies(
            self, company_type: CompanyType) -> List[Dict[str, str]]:
        """Get all unique companies"""
        company_codes = self._auction_collection.distinct(
            f'{company_type.value}_code')
        return [{
            'code':
            code,
            'name':
            self._auction_collection.find_one({
                f'{company_type.value}_code':
                code
            }).get(f'{company_type.value}_name')
        } for code in company_codes]
