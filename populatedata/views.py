from django.views import View
from .models import User, ActivityPeriod
from django.http import HttpResponse
import json


# api to fetch users and it's acticity information
class UserActivityDetails(View):
    def get(self, request):
        members, data = {}, {}
        members_list =[]
        users = User.objects.all()
        # if no users in db
        if not users:
            return HttpResponse("users entries are not available ", \
                                content_type='application/json', status=200)
        # if users then fetch all objects of ActivityPeriod
        activity_info = ActivityPeriod.objects.select_related('user').all()
        data['ok'] = True
        for user in users :
            filtered_activity_info = activity_info.filter(user=user.user_id)
            activity_periods_list = []
            members = user.as_dict() # add user info in dictionary
            for ele in filtered_activity_info:
                activity_periods = {}
                activity_periods['start_time'] = ele.start_time
                activity_periods['end_time'] = ele.end_time
                activity_periods_list.append(activity_periods) # add activity info of user
            members['activity_periods'] = activity_periods_list
            members_list.append(members.copy())
            data['members'] = members_list
        json_data = json.dumps(data, indent = 4, default=str)
        return HttpResponse(json_data, content_type='application/json', status=200)