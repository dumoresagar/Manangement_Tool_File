from .models import Board,Task
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta :
        model = Board
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta :
        model = Task
        fields = '__all__'