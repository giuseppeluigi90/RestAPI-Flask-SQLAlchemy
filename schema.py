from flask_marshmallow import Marshmallow

ma = Marshmallow()

class AccountSchema(ma.Schema):
    class Meta:
        fields = ('name','address','email')

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)