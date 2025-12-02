from flask_smorest import Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields
from models import db
from models.record import RecordModel
from models.category import CategoryModel
from models.user import UserModel

blp = Blueprint("Records", "records", description="Expense records")

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Float(required=True)
    description = fields.Str()
    category_id = fields.Int(required=True)
    user_id = fields.Int(required=True)

@blp.route("/record")
class RecordList(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self):
        return RecordModel.query.all()

    @blp.arguments(RecordSchema)
    @blp.response(201, RecordSchema)
    def post(self, data):
        # Check if user exists
        if not UserModel.query.get(data["user_id"]):
            abort(400, message="User does not exist.")
        category = CategoryModel.query.get(data["category_id"])

        # Check if category exists
        if not category:
            abort(400, message="Category does not exist.")

        # Check if the owner of the category and the user doing the request are the same user
        if category.user_id is not None and category.user_id != data["user_id"]:
            abort(403, message="You cannot use someone else's personal category.")

        rec = RecordModel(**data)
        db.session.add(rec)
        db.session.commit()
        return rec