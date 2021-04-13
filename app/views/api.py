import flask
from flask import (
    Blueprint, current_app, flash, g, redirect, render_template, request,
    send_file, session, url_for, Response, jsonify
)
from urllib.parse import urljoin
from schema import *
from models import Scrapers
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/dashboard', methods=['GET'])
def dashbossard():
    return "Hello Dashboard"
    # return render_template('dashboard/home.html')

@blueprint.route('/register', methods=['GET'])
def register():
    return "Hello Registers"
    # return render_template('dashboard/home.html')



# Registers
@blueprint.route('/scrapers', methods=['GET', 'POST'])
def get_scrapers():
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


@blueprint.route('/scrapers/<id>', methods=['GET'])
def get_scraper(id):
    if request.method == 'GET':
        scraper = Scrapers.query.get(id)
        return scraper_schema.jsonify(scraper)


@blueprint.route('/scrapers/<id>', methods=['PUT'])
def update_scrapers(id):
    scraper = Scrapers.query.get(id)

    created_at = request.json['created_at']
    updated_at = request.json['updated_at']
    objective_id = request.json['objective_id']
    target = request.json['target']
    params = request.json['params']
    structure = request.json['structure']
    status = request.json['status']

    scraper.created_at = created_at
    scraper.updated_at = updated_at
    scraper.objective_id = objective_id
    scraper.target = target
    scraper.params = params
    scraper.structure = structure
    scraper.status = status

    db.session.commit()
    return scraper_schema.jsonify(scraper)
