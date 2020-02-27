from sqlalchemy import (
    Integer,
    Column,
    Sequence,
    Unicode,
    ForeignKey,
    String,
)
from sqlalchemy.orm import relationship
from . import _base


class Person(_base):
    __tablename__ = 'person'
    id = Column(Integer, Sequence('person_id_seq'), primary_key=True, nullable=False)
    english_name = Column(Unicode(120))
    chinese_name = Column(Unicode(120))

    # one to many bidirectional relationships
    job_histories = relationship("JobHistory", back_populates="person")


class JobHistory(_base):
    __tablename__ = 'job_history'
    id = Column(Integer, Sequence('person_id_seq'), primary_key=True, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    title = Column(String(120))
    company = Column(Unicode(120))

    # one to many bidirectional relationships
    person = relationship("Person", back_populates="job_histories")
