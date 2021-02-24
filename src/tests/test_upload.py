import json
import os

import pytest


@pytest.mark.parametrize(
    "file_path, status_code, message",
    [
        [os.path.join("crawler", "dafiti.csv"), 201, "CSV file imported"],
        [
            os.path.join("src","tests","test_data", "dafiti.csv"),
            201,
            "CSV file imported"],
    ],
)
def test_upload_valid_file(test_app, test_database, file_path, status_code, message):
    """
    Given a dev wants to import data into the database
    When he sends out a csv file
    Then the system must insert into the database
    """
    client = test_app.test_client()
    with open(file_path, "rb") as csv_file:
        response = client.post(
            "/data/upload", data={"file": csv_file}, content_type="multipart/form-data"
        )
    data = json.loads(response.data.decode())

    assert response.status_code == status_code
    assert data["message"] == message


@pytest.mark.parametrize(
    "file_name, status_code, message",
    [
        ["troll", 415, "Not a CSV file"],
        ["troll_large_file.csv", 413, "File size not propper, 1MB limit"],
        ["wrong_price.csv", 400, "Failed to import data"],
        [
            "wrong_data_format.csv",
            418,
            "I'm a teapot (File not propper, search for a data.csv.sample)",
        ],
    ],
)
def test_upload_invalid(test_app, test_database, file_name, status_code, message):
    """
    Given a dev wanting to upload data into the database via csv
    When he sends tout the csv file
    Then the system must return error with it's not a propper csv

    Test cases :
        - invalid file, not a .csv
        - large file (upload limit set to 1MB)
        - wrong price format in the CSV
    """
    client = test_app.test_client()
    test_data_path = os.path.join("src", "tests", "test_data", file_name)
    with open(test_data_path, "rb") as test_file:
        response = client.post(
            "/data/upload",
            data={"file": test_file},
            content_type="multipart/form-data",
        )
    data = json.loads(response.data.decode())
    assert response.status_code == status_code
    assert data["message"] == message
