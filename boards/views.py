from django.shortcuts import render , get_object_or_404
from .models import *
from django.http import JsonResponse
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

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
    
class BoardDetails(APIView):
    def get(self , request , board_id):
        board = get_object_or_404(Board , pk = board_id)
        data = BoardSerializer(board).data
        return Response(data)

class BoardTopics(APIView):
    def get(self , request , board_id):
         board = get_object_or_404(Board , pk=board_id)
         topics = board.topics.order_by('-created_dt').annotate(comments=Count('posts'))
         data = TopicsSerializer(topics ,many=True).data
         return Response(data)
     
    def post(self , request , board_id):
        serializer = TopicsSerializer(data = request.data)
        topic_detial = request.data
        if serializer.is_valid():
            topic = serializer.save()
            post_serializer = PostSerializer(data = {
                "message":topic_detial['message'],
                "topic":topic.pk , 
                "created_by":topic.created_by , 
                "created_dat":topic.created_dt , 
                "updated_by":topic.updated_by,
                "updated_dt":topic.updated_dt,
            })
            if post_serializer.is_valid():
                post_serializer.save()
            return Response(serializers.data , status = status.HTTP_201_CREATED)
        return Response(serializers.data , status= status.HTTP_400_BAD_REQUEST)