import unittest

from . import _sessions
from .models import Person, JobHistory
from .factories import PersonFactory


class ModelTest(unittest.TestCase):

    def setUp(self):
        self.scoped_session = _sessions.get('default')
        self.session = self.scoped_session()

    def test_something(self):
        obj = PersonFactory()
        self.assertEqual([obj], self.session.query(Person).all())
        self.assertTrue(10, self.session.query(JobHistory).count())

    def tearDown(self):
        self.session.rollback()
        # Remove it, so that the next test gets a new Session()
        self.scoped_session.remove()
