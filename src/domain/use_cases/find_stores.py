from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import Store


class FindStores(ABC):

    @abstractmethod
    def search_by_name_or_typestore(self, name: str = None, typestore: str = None) -> Dict[bool, List[Store]]:
        raise Exception("Should implement method: pagination")
