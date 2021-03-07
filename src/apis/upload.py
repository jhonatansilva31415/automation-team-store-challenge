import os

import pandas as pd
import werkzeug
from flask_restx import Namespace, Resource
from werkzeug.datastructures import FileStorage

from src.apis.products.crud import add_product

api = Namespace("data", description="Upload data to database")
upload_parser = api.parser()
upload_parser.add_argument("file", location="files", type=FileStorage, required=True)


@api.route("/upload")
@api.expect(upload_parser)
class Upload(Resource):
    @api.doc(
        responses={
            201: "CSV file imported",
            400: "Failed to import data",
            413: "File size not propper, 1MB limit",
            415: "Not a CSV file",
            418: "I'm a teapot (File not propper, search for a data.csv.sample)",
            500: "Error in the upload of the csv file, contact an admin",
        }
    )
    def post(self):
        """Upload a CSV file to the database, you can see the data.csv.sample for
        more info on the expected format"""
        msg = {"message": "Failed to import data", "status_code": 400}
        try:
            args = upload_parser.parse_args()
            uploaded_file = args["file"]
            # works as well for x.x.x.csv and xcsv
            file_ext = os.path.splitext(uploaded_file.filename)[1]
            if file_ext != ".csv":
                msg = {"message": "Not a CSV file", "status_code": 415}
            else:
                df = pd.read_csv(uploaded_file)
                if "url" in df.columns:
                    try:
                        for index in df.index:
                            row = df.loc[index]
                            null_row = row.isnull().values.all()
                            if not null_row:
                                price = row.get("from")
                                if "R$" in price:
                                    price = price.split("R$ ")[1]
                                    price = price.replace(",", ".")
                                    price = float(price)
                                parsed_product = {
                                    "url": row.get("url"),
                                    "img_url": row.get("img_url"),
                                    "brand": row.get("brand"),
                                    "title": row.get("title"),
                                    "price": price,
                                }
                                add_product(parsed_product)
                                msg = {
                                    "message": "CSV file imported",
                                    "status_code": 201,
                                }
                    except Exception:
                        msg = {"message": "Failed to import data", "status_code": 400}
                else:
                    msg = {
                        "message": "I'm a teapot (File not propper, search for a data.csv.sample)",
                        "status_code": 418,
                    }

            return msg, msg["status_code"]

        except werkzeug.exceptions.RequestEntityTooLarge:
            msg = {
                "message": "File size not propper, 1MB limit",
                "status_code": 413,
            }
            return msg, msg["status_code"]

        except Exception:
            msg = {
                "message": "Error in the upload of the csv file, contact an admin",
                "status_code": 500,
            }
            return msg, msg["status_code"]
