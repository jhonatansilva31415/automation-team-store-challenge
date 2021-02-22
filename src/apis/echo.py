from flask_restx import Namespace, Resource

api = Namespace("test", description="For test purposes only")


@api.route("/echo")
class Echo(Resource):
    @api.doc(
        responses={
            200: "Succcess",
        }
    )
    def get(self):
        return {"echo": "echo"}
