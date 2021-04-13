# -*- coding: utf-8 -*-
import os
from flask import (
    Blueprint, current_app, flash, g, redirect, render_template, request, session, url_for
)

blueprint = Blueprint('scrapers', __name__, url_prefix='/scrapers')


@blueprint.before_request

@blueprint.route('/', methods=['GET'])
def home():
    return render_template('scrapers/home.html')