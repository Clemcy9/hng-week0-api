from django.urls import path
from .views import user_dated_details


urlpatterns = [
    path('user-details/', user_dated_details, name='user_details'),
]