from django.shortcuts import render , get_object_or_404
from .models import *
from django.http import JsonResponse
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.
# def BoardsList(request):
#     boards = Board.objects.all()
#     data = {'Result':list(boards.values('pk','name','description'))}
#     return JsonResponse(data)

class BoardList(APIView):
    def get(self,request):
        boards = Board.objects.all()
        data = BoardSerializer(boards , many=True).data
        return Response(data)
    
    def post(self , request):
        serializers = BoardSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status = status.HTTP_201_CREATED)
        return Response(serializers.errors , status.HTTP_400_BAD_REQUEST)

class BoardTopics(APIView):
    def get(self , request , board_id):
         board = get_object_or_404(Board , pk=board_id)
         topics = board.topics.order_by('-created_dt').annotate(comments=Count('posts'))
         data = TopicsSerializer(topics ,many=True).data
         return Response(data)