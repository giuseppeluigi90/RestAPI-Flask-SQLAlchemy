from models import Scrapers
from schema import *
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://scx:y2K.scx@scx/scxcp'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/scrapers', methods=['GET', 'POST'])
@app.route('/scrapers/<id>', methods=['GET', 'POST', 'PUT'])
def get_scrapers(id=None):
    if request.method == 'POST':
        created_at = request.json['created_at']
        updated_at = request.json['updated_at']
        objective_id = request.json['objective_id']
        target = request.json['target']
        params = request.json['params']
        structure = request.json['structure']
        status = request.json['status']

        nuevo_scraper = Scrapers(created_at, updated_at, objective_id, target, params, structure, status)
        db.session.add(nuevo_scraper)
        db.session.commit()

        return scraper_schema.jsonify(nuevo_scraper)
    
    elif request.method == 'GET':
        all_scrapers = Scrapers.query.all()
        result = scrapers_schema.dump(all_scrapers)
        return jsonify(result)


# Run application
if __name__ == "__main__":
    app.run(debug=True)
