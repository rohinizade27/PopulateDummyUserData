from django.urls import path
from .views import UserActivityDetails

urlpatterns = [
    path('', UserActivityDetails.as_view(), name='user_info'),

]