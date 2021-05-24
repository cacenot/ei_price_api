# pylint: disable=E1101

from typing import List
from mongoengine.queryset.visitor import Q

from src.data.interfaces import StoreRepositoryInterface
from src.domain.models import Store
from src.infra.config import DBConnectionHandler
from src.infra.entities import Store as StoreEntity


class StoreRepository(StoreRepositoryInterface):
    """ Class to manage Store Repository """

    @classmethod
    def search_by_name_or_typestore(cls, name: str = None, typestore: str = None) -> List[Store]:
        # """
        # Search data by name in StoreEntity
        # :param - name: name of the store
        # :return - list of store
        # """

        with DBConnectionHandler():
            try:
                filters = None
                if typestore:
                    filters = Q(typestore=typestore)
                if name:
                    filters = filters & Q(name__icontains=name) if filters else Q(name__icontains=name)

                if filters:
                    stores = StoreEntity.objects.filter(filters).order_by('name')[:50]
                else:
                    stores = StoreEntity.objects.order_by('name')[:50]

                list_of_stores = []
                for store in stores:
                    list_of_stores.append(Store(
                        id=store.id,
                        name=store.name,
                        typestore=store.typestore,
                        typestorename=store.typestorename
                    ))
                return list_of_stores
            except:
                ...

        return []
