from typing import Type

from src.main.interface import RouteInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    http_request = HttpRequest(
        header=request.headers, body=request.json, query=request.args.to_dict()
    )

    try:
        response = api_route.route(http_request)
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
