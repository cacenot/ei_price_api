from src.presenters.controllers import FindProductsController
from src.data.find_product import FindProducts
from src.infra.repositories import ProductRepository


def find_products_composer() -> FindProductsController:
    repository = ProductRepository()
    use_case = FindProducts(repository)
    find_products_route = FindProductsController(use_case)

    return find_products_route
