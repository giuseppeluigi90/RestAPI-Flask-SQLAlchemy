"""
sudo -u postgres createuser scx
sudo -u postgres createdb scxcp
sudo -u postgres psql
postgres=# alter user scx with encrypted password 'y2K.scx';
ALTER ROLE
postgres=# grant all privileges on database scxcp to scx;
"""
from sqlalchemy import create_engine, ForeignKey, Column, \
    Integer, String, Float, JSON, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


db_string = "postgresql://scx:y2K.scx@scx/scxcp"
engine = create_engine(db_string, echo=True)
Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
    password = Column(String)


class Objectives(Base):
    __tablename__ = 'objectives'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    name = Column(String)
    status = Column(Boolean)


class Scrapers(Base):
    __tablename__ = 'scrapers'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    objective_id = Column(Integer, ForeignKey('objectives.id'), nullable=False)
    target = Column(String)
    params = Column(JSON)
    structure = Column(JSON)
    scraper_rel = relationship("Objectives", back_populates="scrapers")
    status = Column(Boolean)


class ScrapersTasks(Base):
    __tablename__ = 'scrapers_tasks'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    scraper_id = Column(Integer, ForeignKey('scrapers.id'), nullable=False)
    comment = Column(String)
    task_at = Column(String)
    scraper_task_rel = relationship("Scrapers", back_populates="scrapers_tasks")
    status = Column(Boolean)


class ScrapersLogs(Base):
    __tablename__ = 'scrapers_logs'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    register_at = Column(DateTime)
    scraper_id = Column(Integer, ForeignKey('scrapers.id'), nullable=False)
    scraper_info = Column(JSON)
    fragments = Column(Integer)
    requests = Column(Integer)
    messages = Column(String)
    scraper_log_rel = relationship("Scrapers", back_populates="scrapers_tasks")
    status = Column(Boolean)


class Invoices(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    invoice_serial = Column(String)
    invoice_number = Column(Integer)
    invoice_amount = Column(Float)
    document_link = Column(String)
    status = Column(Boolean)


class Payments(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    messages_out = Column(JSON)
    messages_in = Column(JSON)
    status = Column(Boolean)


# Account.invoices = relationship("Invoices", order_by = Invoices.id, back_populates = "account")
Base.metadata.create_all(engine)
