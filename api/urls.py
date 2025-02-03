from django.urls import path
from .views import user_dated_details, NumberAPIView


urlpatterns = [
    path('user-details/', user_dated_details, name='user_details'),
    path('classify-number/<str:num>', NumberAPIView.as_view(), name = 'number-api'),
]