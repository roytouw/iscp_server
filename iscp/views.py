# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import random
import TweetController

tweetController = TweetController.TweetController()

class StartView(APIView):
    def get(self, request, *args ,**kw):
        tweetController.search_tweets('islamic state')
        result = ['True']
        response = Response(result, status=status.HTTP_200_OK)
        return response


class FetchView(APIView):
    def get(self, request, *args, **kw):
        result = tweetController.get_sentiment()
        print(result)
        response = Response(result, status=status.HTTP_200_OK)
        return response
