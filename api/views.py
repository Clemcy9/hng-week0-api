from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status
import requests



# {
#   "email": "your-email@example.com",
#   "current_datetime": "2025-01-30T09:30:00Z",
#   "github_url": "<https://github.com/yourusername/your-repo>"
# }
@api_view(['GET'])
def user_dated_details(request):
    return Response({
        "email": "clemcy9@gmail.com",
        "current_datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Clemcy9/hng-week0-api"
    })





# {
#     "number": 371,
#     "is_prime": false,
#     "is_perfect": false,
#     "properties": ["armstrong", "odd"],
#     "digit_sum": 11,  // sum of its digits
#     "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
# }
# Required JSON Response Format (400 Bad Request)
# {
#     "number": "alphabet",
#     "error": true
# }

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n ** 0.5) + 1): # check from 2 to the sqrt of number, a form of mirroring
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    divisor_sum = sum(i for i in range(1,n) if n % i == 0) # sum nums from 1 to n-1 only if n/num =0
    return divisor_sum == n

def sum_of_digits(n):
    return eval('+'.join(n))

def is_armstrong(n:str):
    digits = [int(digit) for digit in n]
    num_digits = len(digits)
    print(f'is_armstrong: {int(n) == sum(digit ** num_digits for digit in digits)}')
    return int(n) == sum(digit ** num_digits for digit in digits)

def is_even_odd(n):
    if int(n) % 2 == 0:
        return 'even'
    else:
        return 'odd'

class NumberAPIView(APIView):
    def get(self, request, num):
        if not num.isdigit():
            return Response({
                "number": "alphabet",
                "error": True
            }, status=status.HTTP_400_BAD_REQUEST)
        
        num_properties = []
        if is_armstrong(num):
            num_properties.append('armstrong')
        num_properties.append(is_even_odd(num))
        print(f'this is numberProp: {num_properties}')

        data = {
            "number": int(num),
            "is_prime": is_prime(int(num)),
            "is_perfect": is_perfect(int(num)),
            "properties": num_properties,
            "digit_sum": sum_of_digits(num),
            "fun_fact": requests.get(f'http://numbersapi.com/{int(num)}').text
        }

        return Response(data=data, status=status.HTTP_200_OK)


