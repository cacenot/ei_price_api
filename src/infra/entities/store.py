from mongoengine import Document, IntField, StringField


class Store(Document):
    meta = {'db-alias': 'ei_price'}

    id = IntField(required=True, primary_key=True)
    name = StringField(max_length=1024, required=True)
    typestore = StringField(max_length=24, required=True)
    typestorename = StringField(max_length=1024, required=True)
