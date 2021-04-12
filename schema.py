from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ScrapersSchema(ma.Schema):
    class Meta:
        fields = ('created_at','updated_at','objective_id','target','params','structure','status')

scraper_schema = ScrapersSchema()
scrapers_schema = ScrapersSchema(many=True)