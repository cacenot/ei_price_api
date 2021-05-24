from typing import Dict, List, Type

from src.data.interfaces import StoreRepositoryInterface as StoreRepository
from src.domain.use_cases import FindStores as FindStoresInterface
from src.domain.models import Store


class FindStores(FindStoresInterface):
    """ Class to define usecase: Find stores """

    def __init__(self, store_repository: Type[StoreRepository]):
        self.store_repository = store_repository

    def search_by_name_or_typestore(self, name: str = None, typestore: str = None) -> Dict[bool, List[Store]]:
        response = None
        validate_entry = all([
            isinstance(name, str) or name is None,
            isinstance(typestore, str) or typestore is None,
        ])

        if validate_entry:
            response = self.store_repository.search_by_name_or_typestore(name=name, typestore=typestore)

        return {"success": validate_entry, "data": response}
