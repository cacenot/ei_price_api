# pylint: disable=E1101
from typing import List, Dict
from decimal import Decimal
from mongoengine.queryset.visitor import Q

from src.data.interfaces import ProductRepositoryInterface
from src.domain.models import Product
from src.infra.config import DBConnectionHandler
from src.infra.entities import Product as ProductEntity


class ProductRepository(ProductRepositoryInterface):
    """ Class to manage product Repository """

    @classmethod
    def pagintation_and_filter(self, store_id: int = None, ean: str = None, category: str = None,
                               limit: int = 50, offset: int = 0):
        # """
        # Search data by name in StoreEntity
        # :param - name: name of the store
        # :return - list of store
        # """

        with DBConnectionHandler():
            try:
                filters = None
                if store_id:
                    filters = Q(store_id=store_id)
                if ean:
                    filters = filters & Q(ean=ean) if filters else Q(ean=ean)
                if category:
                    filters = filters & Q(category=category) if filters else Q(category=category)
                
                if filters:
                    products_count = ProductEntity.objects.filter(filters).count()
                    categories_count = len(list(ProductEntity.objects.filter(filters).aggregate([{
                        '$group': {'_id': '$category'}
                    }])))
                    promotions_count = ProductEntity.objects.filter(filters & Q(category__icontains="promoções")) \
                        .count()
                    products = ProductEntity.objects.filter(filters).order_by('name').limit(limit).skip(offset)
                else:
                    products_count = ProductEntity.objects.count()
                    categories_count = len(list(ProductEntity.objects.aggregate([{
                        '$group': {'_id': '$category'}
                    }])))
                    promotions_count = ProductEntity.objects(category__icontains="promoções").count()
                    products = ProductEntity.objects.order_by('name').limit(limit).skip(offset)

                has_next_page = ((products_count - offset) / limit) > 1

                list_of_products = []
                for product in products:
                    list_of_products.append(Product(
                        ean=product.ean,
                        name=product.name,
                        category=product.category,
                        price=float(product.price) if isinstance(product.price, Decimal) else None,
                        quantity=product.quantity,
                        real_price=float(product.real_price) if isinstance(product.real_price, Decimal) else None,
                        sale_type=product.sale_type,
                        store_id=product.store_id,
                        typestore=product.typestore,
                        typestorename=product.typestorename,
                        unit_type=product.unit_type,
                    ))
                return {
                    "products": list_of_products,
                    "products_count": products_count,
                    "categories_count": categories_count,
                    "promotions_count": promotions_count,
                    "has_next_page": has_next_page
                }
            except Exception as e:
                print(e)
                ...

        return []
