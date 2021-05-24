from typing import Type

from src.main.interface import RouteInterface
from src.domain.use_cases import FindProducts
from src.presenters.helpers import HttpResponse, HttpRequest
from src.presenters.errors import HttpErrors


class FindProductsController(RouteInterface):
    """ Class to define Route to find_products use case """

    def __init__(self, find_products_use_case: Type[FindProducts]):
        self.find_products_use_case = find_products_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpRequest:
        """ Method to call use case """

        response = None

        try:
            store_id = http_request.query.get("store_id")
            if store_id:
                store_id = int(store_id)
            ean = http_request.query.get("ean")
            if ean:
                ean = int(ean)
            category = http_request.query.get("category")
            limit = int(http_request.query.get("limit", '50'))
            offset = int(http_request.query.get("offset", '0'))
            response = self.find_products_use_case.pagintation_and_filter(store_id=store_id, ean=ean, category=category,
                                                                          limit=limit, offset=offset)

            if response["success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])
        except ValueError as err:
            https_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=https_error["status_code"], body={"error": err}
            )
