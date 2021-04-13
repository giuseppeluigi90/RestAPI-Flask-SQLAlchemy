# -*- coding: utf-8 -*-
import os
from flask import Flask, g, redirect, render_template, session, url_for


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    from .views import (
        api, dashboard, register, scrapers, terms
    )
    app.register_blueprint(api.blueprint)
    app.register_blueprint(dashboard.blueprint)
    app.register_blueprint(register.blueprint)
    app.register_blueprint(scrapers.blueprint)
    app.register_blueprint(terms.blueprint)

    # Processors

    # app.context_processor(company_context_processor)
    # app.context_processor(user_context_processor)


    # Handlers

    # @app.errorhandler(404)
    # def page_not_found(e):
    #     return render_template('404.html'), 404


    # @app.errorhandler(500)
    # def page_not_found(e):
    #     return render_template('500.html'), 500

    @app.route('/', methods=['GET'])
    def index():
        return redirect(url_for('dashboard.home'))


    # Flask uploads

    # configure_uploads(
    #     app,
    #     (
    #         app.config['UPLOADED_LOGOS'],
    #         app.config['UPLOADED_PLANS'],
    #         app.config['UPLOADED_EXAMS'],
    #         app.config['UPLOADED_RISKS'],
    #     )
    # )
    # patch_request_class(app, 12 * 1024 * 1024)  # 12 MiB

    return app
