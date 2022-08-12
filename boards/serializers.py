from .models import *
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        
class TopicsSerializer(serializers.ModelSerializer):
    board_name = serializers.CharField(source = "board.name" , required = False)
    creater_name = serializers.CharField(source = "created_by.username" , required = False)
    class Meta:
        model = Topic 
        fields = '__all__'