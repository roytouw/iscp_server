# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import random


class StartView(APIView):
    def get(self, request, *args ,**kw):
        print('starting the search')
        result = ['true']
        response = Response(result, status=status.HTTP_200_OK)
        return response


class FetchView(APIView):
    def get(self, request, *args, **kw):
        result = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        response = Response(result, status=status.HTTP_200_OK)
        return response