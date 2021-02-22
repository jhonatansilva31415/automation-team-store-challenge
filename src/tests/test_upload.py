import json
import os


def test_upload_valid_file(test_app, test_database):
    """
    Given a dev wants to import data into the database
    When he sends out a csv file
    Then the system must insert into the database
    """
    client = test_app.test_client()
    test_data_path = os.path.join("crawler", "dafiti.csv")
    with open(test_data_path, "rb") as csv_file:
        response = client.post(
            "/data/upload", data={"file": csv_file}, content_type="multipart/form-data"
        )
    data = json.loads(response.data.decode())

    assert response.status_code == 201
    assert "CSV file imported" in data["message"]


def test_upload_invalid(test_app, test_database):
    """
    Given a dev wanting to upload data into the database via csv
    When he sends tout the csv file
    Then the system must return error with it's not a propper csv
    """
    client = test_app.test_client()
    test_data_path = os.path.join("src", "tests", "test_data", "troll")
    with open(test_data_path, "rb") as troll_file:
        response = client.post(
            "/data/upload",
            data={"file": troll_file},
            content_type="multipart/form-data",
        )
    data = json.loads(response.data.decode())
    assert response.status_code == 415
    assert "Not a CSV file" in data["message"]


def test_upload_large_file(test_app, test_database):
    """
    Given a sneak dev wanting to upload a large file
    When he sends tout the file
    Then the system must return error
    """
    client = test_app.test_client()
    test_data_path = os.path.join("src", "tests", "test_data", "troll_large_file.csv")
    with open(test_data_path, "rb") as troll_large_file:
        response = client.post(
            "/data/upload",
            data={"file": troll_large_file},
            content_type="multipart/form-data",
        )
    data = json.loads(response.data.decode())
    assert response.status_code == 413
    assert "File size not propper, 1MB limit" in data["message"]


def test_upload_wrong_price(test_app, test_database):
    """
    Given a user that wants to import data into the system
    When he sends tout the file
    If the price is in the wrong format
    Then the system must return error
    """
    client = test_app.test_client()
    test_data_path = os.path.join("src", "tests", "test_data", "wrong_price.csv")
    with open(test_data_path, "rb") as wrong_price:
        response = client.post(
            "/data/upload",
            data={"file": wrong_price},
            content_type="multipart/form-data",
        )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Failed to import data" in data["message"]


def test_upload_wrong_csv(test_app, test_database):
    """
    Given a user that is new to the system and wants to import a csv file
    When he sends out the data
    If the csv doesn't have the propper columns
    Then the system must return a 418 error
    """
    client = test_app.test_client()
    test_data_path = os.path.join("src", "tests", "test_data", "wrong_data_format.csv")
    with open(test_data_path, "rb") as wrong_data_format:
        response = client.post(
            "/data/upload",
            data={"file": wrong_data_format},
            content_type="multipart/form-data",
        )
    data = json.loads(response.data.decode())
    assert response.status_code == 418
    assert (
        "I'm a teapot (File not propper, search for a data.csv.sample)"
        in data["message"]
    )
