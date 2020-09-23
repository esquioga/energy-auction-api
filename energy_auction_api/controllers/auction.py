"""Module exposing Auction controller"""
from logging import getLogger
from typing import List, Dict
from enum import Enum

from pymongo.collection import Collection

from ..adapters.auctions import parse_xsl

LOGGER = getLogger(__name__)


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
        update_response = self._auction_collection.update_many(auction_data,
                                                               upsert=True)
        LOGGER.info(update_response.raw_result())

    def get_unique_companies(
            self, company_type: CompanyType) -> List[Dict[str, str]]:
        """Get all unique companies"""
        company_codes = self._auction_collection.distinct(
            f'{company_type.value}_code')
        return [{
            'code':
            code,
            'name':
            self._auction_collection.find_one(
                {f'{company_type.value}_code':
                 code}.get(f'{company_type.value}_company_name'))
        } for code in company_codes]
