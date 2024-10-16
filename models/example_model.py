import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base

class ExampleModel(Base):
    _tablename_ = 'example_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
