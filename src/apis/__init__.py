from flask_restx import Api

from .echo import api as echo_ns
from .products.products import api as products_ns
from .upload import api as upload_ns

api = Api(
    title="Automation Challenge",
    version="1.1",
    description="Simple CRUD app for a fashion related marketplace",
)

api.add_namespace(echo_ns)
api.add_namespace(upload_ns)
api.add_namespace(products_ns)
