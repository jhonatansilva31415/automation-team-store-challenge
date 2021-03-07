from src.apis.products.models import Product
from src.app import db


def add_product(parsed_product):
    """
    Adds a products into the database
    It also checks if already exists by the URL (not the best way for sure)
    """
    url = parsed_product["url"]
    img_url = parsed_product["img_url"]
    brand = parsed_product["brand"]
    title = parsed_product["title"]
    price = parsed_product["price"]
    product_exists = Product.query.filter_by(url=url).first()
    if product_exists:
        product = []
    else:
        product = Product(
            url=url, img_url=img_url, brand=brand, title=title, price=price
        )
        db.session.add(product)
        db.session.commit()

    return product


def get_all_products():
    """ Returns all products that are active """
    return Product.query.filter_by(is_active=True).all()


def get_product_by_id(product_id):
    """ Get a product by it's id """
    return Product.query.filter_by(id=product_id).first()


def update_product(product, requested):
    """ Updates a product """
    product.url = requested["url"]
    product.img_url = requested["img_url"]
    product.brand = requested["brand"]
    product.title = requested["title"]
    product.price = requested["price"]
    db.session.commit()
    return product


def delete_product(product):
    """ Update the status of the product to inactive """
    product.is_active = False
    db.session.commit()
    return product
