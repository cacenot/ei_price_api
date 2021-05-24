from typing import Type

from src.main.interface import RouteInterface
from src.domain.use_cases import FindStores
from src.presenters.helpers import HttpResponse, HttpRequest
from src.presenters.errors import HttpErrors


class FindStoresController(RouteInterface):
    """ Class to define Route to find_stores use case """

    def __init__(self, find_stores_use_case: Type[FindStores]):
        self.find_stores_use_case = find_stores_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpRequest:
        """ Method to call use case """

        response = None

        name = http_request.query.get("name")
        typestore = http_request.query.get("typestore")
        response = self.find_stores_use_case.search_by_name_or_typestore(name=name, typestore=typestore)

        if response["success"] is False:
            https_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=https_error["status_code"], body=https_error["body"]
            )

        return HttpResponse(status_code=200, body=response["data"])
