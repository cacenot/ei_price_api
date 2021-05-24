from typing import Dict, List, Type

from src.data.interfaces import ProductRepositoryInterface as ProductRepository
from src.domain.use_cases import FindProducts as FindProductsInterface
from src.domain.models import Product


class FindProducts(FindProductsInterface):
    """ Class to define usecase: Find products """

    def __init__(self, product_repository: Type[ProductRepository]):
        self.product_repository = product_repository

    def pagintation_and_filter(self, store_id: int = None, ean: int = None, category: str = None,
                               limit: int = 50, offset: int = 0):
        response = None
        validate_entry = all([
            (isinstance(store_id, int) or store_id is None),
            (isinstance(ean, int) or ean is None),
            (isinstance(category, str) or category is None),
            isinstance(limit, int),
            isinstance(offset, int),
        ])

        if validate_entry:
            response = self.product_repository.pagintation_and_filter(store_id=store_id, ean=ean, category=category,
                                                                      limit=limit, offset=offset)

        return {"success": validate_entry, "data": response}
