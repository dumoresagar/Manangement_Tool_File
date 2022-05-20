from django.shortcuts import render,redirect
from .models import Board,Task
from .serializers import BoardSerializer,TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url='login')
class CreateBoardView(APIView):
    def get(self, request):
        board = Board.objects.all()
        serializer = BoardSerializer(board, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'board create successfully'},serializer.data, status=status.HTTP_200_OK,redirect_to='listboard')
        return Response(serializer.errors)


class ListBoardsView(APIView):
    def get(self, request, id):
        if id:
            try:
                board = Board.objects.get(id=id)
            except Board.DoesNotExist:
                return Response({'msg': 'record doest not exist'})
            serializer = BoardSerializer(board)
            return Response(serializer.data)
        return Response({'msg': 'please provite the id'})


class CreateTaskView(APIView):
    def get(self, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ListTaskView(APIView):
    def get(self, request, id):
        if id:
            try:
                task = Task.objects.get(id=id)
            except Task.DoesNotExist:
                return Response({'msg': 'record doest not exist'})
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response({'msg': 'please provide the id'})

    def put(self, request, id):
        if id:
            try:
                task = Task.objects.get(id=id)
            except Task.DoesNotExist:
                return Response({'msg': 'record doest not exist'})
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({'msg': 'please send id'})
