import factory.fuzzy
from .models import Person, JobHistory
from . import _sessions

default_session = _sessions.get('default')


names = {
    'John': '王大明',
    'Tom': '湯碼士',
}


class JobHistoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = JobHistory
        sqlalchemy_session = default_session

    title = factory.Faker('job')
    company = factory.Faker('company')


class PersonFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Person
        sqlalchemy_session = default_session

    id = factory.Sequence(lambda n: n)
    english_name = factory.fuzzy.FuzzyChoice(names.keys(), lambda o: o)
    chinese_name = factory.LazyAttribute(lambda o: names.get(o.english_name))

    # relations
    job_histories = factory.RelatedFactoryList(JobHistoryFactory, 'person', size=10)
