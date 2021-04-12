from flask import (
    Blueprint, current_app, flash, g, redirect, render_template, request,
    send_file, session, url_for, Response
)
from urllib.parse import urljoin



blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/dashboard', methods=['GET'])
def dashbossard():
    return "Hello Dashboard"
    # return render_template('dashboard/home.html')

@blueprint.route('/register', methods=['GET'])
def register():
    return "Hello Registers"
    # return render_template('dashboard/home.html')
