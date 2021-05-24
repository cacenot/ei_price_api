from faker import Faker

from src.domain.test import mock_product
from src.infra.entities import Product
from src.infra.config import DBConnectionHandler
from .product_repository import ProductRepository


faker = Faker()
product_repository = ProductRepository()


def test_paginate_and_filter_products():
    """ Should find a list of stores filtered by ean, category or store_id """
    with DBConnectionHandler():
        unique_category = "Ofertas"
        unique_store_id = 8964968411
        unique_ean = None

        filter_mocks_qty = 2
        fake_mocks_qty = 3
        while filter_mocks_qty > 0:
            mock = mock_product()
            unique_ean = mock.ean
            product = Product(
                ean=mock.ean,
                category=unique_category,
                name=mock.name,
                price=mock.price,
                real_price=mock.real_price,
                quantity=mock.quantity,
                store_id=unique_store_id,
                sale_type=mock.sale_type,
                unit_type=mock.unit_type,
                typestore=mock.typestore,
                typestorename=mock.typestorename
            )
            product.save()
            filter_mocks_qty -= 1

        while fake_mocks_qty > 0:
            mock = mock_product()
            product = Product(
                ean=mock.ean,
                category=mock.category,
                name=mock.name,
                price=mock.price,
                real_price=mock.real_price,
                quantity=mock.quantity,
                store_id=mock.store_id,
                sale_type=mock.sale_type,
                unit_type=mock.unit_type,
                typestore=mock.typestore,
                typestorename=mock.typestorename
            )
            product.save()
            fake_mocks_qty -= 1

        query_product_by_store_id = product_repository.pagintation_and_filter(store_id=unique_store_id)
        query_product_by_ean = product_repository.pagintation_and_filter(ean=unique_ean)
        query_product_by_category = product_repository.pagintation_and_filter(category=unique_category)
        query_product_by_store_id_and_category = product_repository.pagintation_and_filter(store_id=unique_store_id,
                                                                                           category=unique_category)
        query_product_by_store_id_with_limit = product_repository.pagintation_and_filter(store_id=unique_store_id,
                                                                                         limit=1)
        query_product_by_store_id_with_offset = product_repository.pagintation_and_filter(store_id=unique_store_id,
                                                                                          offset=1)

        assert len(query_product_by_store_id) == 2
        assert len(query_product_by_ean) == 1
        assert len(query_product_by_category) == 2
        assert len(query_product_by_store_id_and_category) == 2
        assert len(query_product_by_store_id_with_limit) == 1
        assert len(query_product_by_store_id_with_offset) == 1
