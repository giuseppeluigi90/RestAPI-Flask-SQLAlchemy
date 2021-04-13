from flask import Flask
from scrapers_routes import scrapers
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Config DB
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://scx:y2K.scx@scx/scxcp'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Register blueprint
app.register_blueprint(scrapers)

# Run application
if __name__ == "__main__":
    app.run(debug=True)
