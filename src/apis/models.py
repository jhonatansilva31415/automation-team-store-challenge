import os

from src.app import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(2048), nullable=False)
    img_url = db.Column(db.String(2048), nullable=False)
    brand = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    dafiti_id = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)
        try:
            # unique number for each product in the URL
            url_without_extension = os.path.splitext(self.url)[0]
            self.dafiti_id = url_without_extension.split("-")[-1]
        except Exception:
            self.dafiti_id = ""
