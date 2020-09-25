from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True, editable=False, max_length=10)
    real_name = models.CharField(max_length=64)
    time_zone = models.CharField(max_length=64)

    def __str__(self):
        return self.real_name

    def as_dict(self):
        user_dict = dict()
        user_dict['id'] = self.user_id
        user_dict['real_name'] = self.real_name
        user_dict['tz'] = self.time_zone
        return user_dict


class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.real_name


