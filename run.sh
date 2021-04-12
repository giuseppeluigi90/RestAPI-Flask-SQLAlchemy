#!/bin/bash

export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run --port=5555 --host=0.0.0.0