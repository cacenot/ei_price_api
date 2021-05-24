from flask import Blueprint, jsonify, request

from src.main.composer import (
    find_stores_composer,
    find_products_composer
)
from src.main.adapters import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/stores", methods=["GET"])
def finder_stores():
    """ find stores route """

    data = {}
    response = flask_adapter(request=request, api_route=find_stores_composer())

    if response.status_code < 300:
        data = []

        for element in response.body:
            data.append(
                {
                    "id": element.id,
                    "name": element.name,
                    "typestore": element.typestore,
                    "typestorename": element.typestorename,
                }
            )

        return jsonify({"data": data}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/products", methods=["GET"])
def finder_products():
    """ find products route """

    data = {}
    response = flask_adapter(request=request, api_route=find_products_composer())

    if response.status_code < 300:
        data = []

        for element in response.body["products"]:
            data.append(
                {
                    "ean": element.ean,
                    "category": element.category,
                    "name": element.name,
                    "price": element.price,
                    "quantity": element.quantity,
                    "real_price": element.real_price,
                    "store_id": element.store_id,
                    "sale_type": element.sale_type,
                    "unit_type": element.unit_type,
                    "typestore": element.typestore,
                    "typestorename": element.typestorename,
                }
            )

        return jsonify({
            "has_next_page": response.body["has_next_page"],
            "products_count": response.body["products_count"],
            "categories_count": response.body["categories_count"],
            "promotions_count": response.body["promotions_count"],
            "data": data
        }), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
