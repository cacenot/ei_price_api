import decimal
from mongoengine import Document, IntField, StringField, DecimalField


class Product(Document):
    ean = IntField(max_length=13, primary_key=True)
    category = StringField(max_length=255, required=True)
    name = StringField(max_length=1024, required=True)
    price = DecimalField(precision=2, min_value=0, rounding=decimal.ROUND_CEILING, required=True)
    real_price = DecimalField(precision=2, min_value=0, rounding=decimal.ROUND_CEILING, required=True)
    quantity = IntField(required=True)
    store_id = IntField(required=True)
    sale_type = StringField(max_length=16, required=True)
    unit_type = StringField(max_length=16, required=True)
    typestore = StringField(max_length=24, required=True)
    typestorename = StringField(max_length=1024, required=True)
