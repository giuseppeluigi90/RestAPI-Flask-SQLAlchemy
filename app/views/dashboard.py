# -*- coding: utf-8 -*-
import os
from flask import (
    Blueprint, current_app, flash, g, redirect, render_template, request, session, url_for
)

blueprint = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@blueprint.before_request

@blueprint.route('/', methods=['GET'])
def home():
    return render_template('dashboard/home.html')