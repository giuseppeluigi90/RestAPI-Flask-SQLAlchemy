from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Float, JSON, DateTime, Boolean
from sqlalchemy.orm import relationship

db = SQLAlchemy()


# Model for Scrapers DB
class Scrapers(db.Model):    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    objective_id = Column(Integer)
    target = Column(String)
    params = Column(JSON)
    structure = Column(JSON)
    status = Column(Boolean)

    def __init__(self, create_at, updated_at, objective_id, target, params, structure, status):
        self.create_at = created_at
        self.updated_at = updated_at
        self.objective_id = objective_id
        self.target = target
        self.params = params
        self.structure = structure
        self.status = status