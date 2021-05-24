from abc import ABC, abstractmethod
from typing import List

from src.domain.models import Store


class StoreRepositoryInterface(ABC):

    @abstractmethod
    def search_by_name_or_typestore(self, name: str = None, typestore: str = None) -> List[Store]:
        raise Exception("Method not implemented")
