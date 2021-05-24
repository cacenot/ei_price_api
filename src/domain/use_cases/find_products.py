from abc import ABC, abstractmethod
from typing import List, Dict

from src.domain.models import Product


class FindProducts(ABC):

    @abstractmethod
    def pagintation_and_filter(self, store_id: int = None, ean: int = None, category: str = None,
                               limit: int = 50, offset: int = 0):
        raise Exception("Should implement method: pagination")
