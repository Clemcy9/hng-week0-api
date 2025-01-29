from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def user_dated_details(request):
    return Response({
        "email": "clemcy9@gmail.com",
        "current_datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": ""
    })

# {
#   "email": "your-email@example.com",
#   "current_datetime": "2025-01-30T09:30:00Z",
#   "github_url": "<https://github.com/yourusername/your-repo>"
# }