import copy

from src.apis.models import Product

test_product = {
    "url": "test_product_url",
    "img_url": "test_product_img_url",
    "brand": "test_product_brand",
    "title": "test_product_title",
    "price": 6.66,
}


def test_add_product(test_app, test_database):
    """
    Given a user wants to add a new product into the database
    When he sends out the data
    Then the system must return a the new product ( or update it )
    """

    client = test_app.test_client()
    response = client.post(
        "/products", json=test_product, content_type="application/json"
    )

    data = response.json
    assert response.status_code == 201
    for key in test_product.keys():
        assert data[key] == test_product[key]


def test_add_invalid_product(test_app, test_database):
    """
    Given a user wanting to add a new product into the database
    When he sends out incorrect data
    Then the system must reject the creation of the product
    """
    client = test_app.test_client()
    response = client.post(
        "/products",
        json={
            "url": 1,
            "brand": -3,
            "title": "",
            "price": 0,
        },
        content_type="application/json",
    )
    assert response.status_code == 400

    response = client.post("/products", json={}, content_type="application/json")
    assert response.status_code == 400

    response = client.post(
        "/products",
        json={
            "url": "",
            "brand": "",
            "title": "",
            "price": 0,
        },
        content_type="application/json",
    )
    data = response.json
    assert response.status_code == 400
    assert data["message"] == "Input payload validation failed"


def test_add_existing_product(test_app, test_database):
    """
    Given a user wanting to add a new product into the database
    When he sends out the data
    Then the system must reject the creation of the product
    If the product already exists
    """
    client = test_app.test_client()
    for _ in range(2):
        response = client.post(
            "/products", json=test_product, content_type="application/json"
        )
    data = response.json
    assert response.status_code == 409
    assert data == []


def test_get_product_by_id(test_app, test_database, add_product):
    """
    Given a user wants to get a product
    When he sends out the id of the product
    Then the system must return the product
    If exists
    """
    test_database.session.query(Product).delete()
    product = add_product(test_product)
    client = test_app.test_client()
    response = client.get(f"/products/{product.id}")
    data = response.json
    assert response.status_code == 200
    for key in test_product.keys():
        assert data[key] == test_product[key]


def test_get_all_products(test_app, test_database, add_product):
    """
    Given a user that wants access to all products
    When he sends out a request
    Then the system must return all products
    """
    test_database.session.query(Product).delete()
    products = []
    for index in range(10):
        test_product.update({"price": round(0.37 * (index + 1), 2)})
        product = add_product(test_product)
        products.append(copy.deepcopy(test_product))
    client = test_app.test_client()
    response = client.get("/products")
    data = response.json
    assert response.status_code == 200
    assert len(data) == 10
    for index, product in enumerate(products):
        for key in test_product.keys():
            if key == "price":
                assert data[index][key] == product[key]


def test_update_product(test_app, test_database, add_product):
    """
    Given a user that wants to update a product
    When he sends out a request
    Then the system must update the product and return it back
    If the product exists
    """
    test_database.session.query(Product).delete()
    product = add_product(test_product)
    client = test_app.test_client()
    # Updates the product
    updated_product = copy.deepcopy(test_product)
    updated_product.update({"price": 1.11})
    response = client.put(
        f"/products/{product.id}",
        json=updated_product,
        content_type="application/json",
    )
    data = response.json
    assert response.status_code == 200
    for key in test_product.keys():
        assert data[key] == updated_product[key]

    # Go and get updated product
    response = client.get(f"/products/{product.id}")
    data = response.json
    assert response.status_code == 200
    for key in test_product.keys():
        assert data[key] == updated_product[key]


def test_update_product_invalid_data(test_app, test_database, add_product):
    """
    Given a user that wants to update a product
    When he sends out a request
    Then the system must update the product and return it back
    If the data is correct
    """
    test_database.session.query(Product).delete()
    product = add_product(test_product)
    client = test_app.test_client()
    # Updates the product
    response = client.put(
        f"/products/{product.id}",
        json={
            "url": "",
            "brand": "test_brand_put",
            "title": "test_title_put",
            "price": 1.11,
        },
        content_type="application/json",
    )
    data = response.json
    assert response.status_code == 400
    assert data["message"] == "Input payload validation failed"


def test_delete_product(test_app, test_database, add_product):
    """
    Given a user that wants to delete a product
    When he sends out a request
    Then the system must update the product as inactive
    If the product exists
    """
    test_database.session.query(Product).delete()
    product = add_product(test_product)
    client = test_app.test_client()
    response = client.delete(f"/products/{product.id}")
    data = response.json

    assert response.status_code == 200
    assert not data["is_active"]

    response = client.get("/products")
    data = response.json
    assert response.status_code == 200
    # Assure that the inactive product is not being list in the get_all endpoint
    assert len(data) == 0
