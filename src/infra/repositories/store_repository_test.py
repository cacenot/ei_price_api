from src.domain.test import mock_store
from src.infra.entities import Store
from src.infra.config import DBConnectionHandler
from .store_repository import StoreRepository

store_repository = StoreRepository()


def test_search_stores():
    """ Should find a list of stores filtered by name """
    with DBConnectionHandler():
        mock_store1 = mock_store()
        mock_store2 = mock_store()
        store1 = Store(id=mock_store1.id, name=mock_store1.name, typestore=mock_store1.typestore,
                       typestorename=mock_store1.typestorename)
        store2 = Store(id=mock_store2.id, name=mock_store2.name, typestore=mock_store2.typestore,
                       typestorename=mock_store2.typestorename)
        store1.save()
        store2.save()

        query_stores1 = store_repository.search_by_name(name=mock_store1.name[1:4])
        query_stores2 = store_repository.search_by_name(name=mock_store2.name[1:4])

        assert len(query_stores1) > 0
        assert len(query_stores2) > 0
