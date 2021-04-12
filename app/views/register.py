# -*- coding: utf-8 -*-
import os
from flask import (
    Blueprint, current_app, flash, g, redirect, render_template, request, session, url_for
)

blueprint = Blueprint('register', __name__, url_prefix='/register')


@blueprint.before_request

@blueprint.route('/', methods=['GET'])
def home():
    return render_template('register/home.html')