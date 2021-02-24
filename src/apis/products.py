import copy

from flask import request
from flask_restx import Namespace, Resource, fields

from src.apis.crud import (
    add_product,
    delete_product,
    get_all_products,
    get_product_by_id,
    update_product,
)

api = Namespace("products", description="Product Resource")

base_product = {
    "url": fields.String(min_length=1, max_length=2048, required=True),
    "img_url": fields.String(min_length=1, max_length=2048, required=True),
    "brand": fields.String(min_length=1, max_length=128, required=True),
    "title": fields.String(min_length=1, max_length=128, required=True),
    "price": fields.Float(min=0, required=True),
}

marshal_product = copy.deepcopy(base_product)
marshal_product.update(
    {
        "id": fields.Integer(readOnly=True),
        "is_active": fields.Boolean(),
        "dafiti_id": fields.String(),
        "created_on": fields.DateTime(),
        "updated_on": fields.DateTime(),
    }
)

product = api.model("Product", base_product)
product_marshal = api.model("MarshalProduct", marshal_product)


@api.route("")
class ProductsList(Resource):
    @api.marshal_with(product_marshal, as_list=True)
    @api.doc(
        responses={
            200: "Success",
        }
    )
    def get(self):
        """
        Get all products
        """
        products = get_all_products()
        return products

    @api.marshal_with(product_marshal, as_list=True)
    @api.expect(product, validate=True)
    @api.doc(
        responses={
            201: "Product <product_id> created",
            400: "Input payload validation failed",
        }
    )
    def post(self):
        """
        Adds a product to the database
        """
        data = request.get_json()
        requested_product = {
            "url": data.get("url"),
            "img_url": data.get("img_url"),
            "brand": data.get("brand"),
            "title": data.get("title"),
            "price": data.get("price"),
        }
        product = add_product(requested_product)
        product_already_exists = product == []
        if product_already_exists:
            return product, 409
        else:
            return product, 201


@api.route("/<int:product_id>")
class Products(Resource):
    @api.marshal_with(product_marshal)
    @api.doc(responses={200: "Success", 404: "Product <product_id> does not exist"})
    def get(self, product_id):
        """
        Get a product by id
        """
        product = get_product_by_id(product_id)
        if not product:
            api.abort(404, f"Product {product_id} does not exist")
        return product

    @api.marshal_with(product_marshal)
    @api.expect(product, validate=True)
    @api.doc(
        responses={
            200: "Product <product_id> was updated",
            404: "Product <product_id> does not exist",
        }
    )
    def put(self, product_id):
        """
        Updates a product given an id
        """
        data = request.get_json()
        url = data.get("url")
        brand = data.get("brand")
        title = data.get("title")
        price = data.get("price")
        product = get_product_by_id(product_id)
        if not product:
            api.abort(404, f"Product {product_id} does not exist")

        product = update_product(product, url, brand, title, price)
        return product

    @api.marshal_with(product_marshal, as_list=True)
    @api.doc(
        responses={
            200: "Product <product_id> was deleted",
            404: "Product <product_id> does not exist",
        }
    )
    def delete(self, product_id):
        """
        Deletes a product given an id
        """
        product = get_product_by_id(product_id)
        if product:
            product = delete_product(product)
            return product
        else:
            api.abort(404, f"Product {product_id} does not exist")
