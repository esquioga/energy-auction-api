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

    def get_company_detail(self, company_code: str):
        result = {
            'name': '',
            'total_earnings': 0,
            'total_engery_negotiated': 0,
            'auctions': []
        }
        for item in self._auction_collection.find(
            {"seller_code": int(company_code)}):
            if not result['name']:
                result['name'] = item.get('seller_name', '')
            financial_amount = item.get('financial_amount', 0)
            energy_amount = item.get('negotiated_energy_by_contract', 0)
            result['total_earnings'] += financial_amount
            result['total_engery_negotiated'] += item.get(
                'negotiated_energy_by_contract', 0)
            result['auctions'].append({
                'id':
                item.get('auction_id'),
                'auction_name':
                item.get('auction'),
                'buyer':
                item.get('buyer_name'),
                'financial_amount':
                financial_amount,
                'energy_amount':
                energy_amount,
                'ice':
                item.get('ice'),
                'price_updated':
                item.get('price_updated'),
                'initial_date':
                item.get('initial_date'),
                'final_date':
                item.get('final_date')
            })

        return result
