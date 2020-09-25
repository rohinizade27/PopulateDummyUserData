import factory
from .models import User, ActivityPeriod
from datetime import datetime as dt
import pytz


# factory allows you to create templates for producing valid objects and Faker generates fake data
class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    real_name = factory.Faker('name')
    time_zone = factory.Faker('timezone')
    user_id = factory.Faker('bothify',text='?##?????#')


class ActivityPeriodFactory(factory.DjangoModelFactory):

    class Meta:
        model = ActivityPeriod
    user = factory.SubFactory(UserFactory)
    start_time = factory.Faker('date_time_this_year', tzinfo=pytz.utc)

    @factory.lazy_attribute
    def end_time(self):
        return factory.Faker('date_time_between_dates',
                             datetime_start=self.start_time,
                             datetime_end=dt.now(),
                             tzinfo=pytz.utc).generate({})


