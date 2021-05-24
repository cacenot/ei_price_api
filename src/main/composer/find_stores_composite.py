from src.presenters.controllers import FindStoresController
from src.data.find_store import FindStores
from src.infra.repositories import StoreRepository


def find_stores_composer() -> FindStoresController:
    repository = StoreRepository()
    use_case = FindStores(repository)
    find_stores_route = FindStoresController(use_case)

    return find_stores_route
