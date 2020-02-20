from sqlalchemy import (
    Integer,
    Column,
    Sequence,
    Unicode,
)
from . import _base


class Example(_base):
    """Example model"""
    __tablename__ = 'example'
    id = Column(Integer, Sequence('config_id_seq'), primary_key=True, nullable=False)
    name = Column(Unicode(5))
