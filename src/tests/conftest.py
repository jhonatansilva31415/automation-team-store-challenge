import pytest

from src.app import create_app, db

from src.apis.products.models import Product  # noqa  # isort:skip


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("src.config.TestingConfig")
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def add_product():
    """
    Insert a product in the database for test purposes
    """

    def _add_product(data):

        product = Product(
            url=data["url"],
            img_url=data["img_url"],
            brand=data["brand"],
            title=data["title"],
            price=data["price"],
        )
        db.session.add(product)
        db.session.commit()
        return product

    return _add_product
