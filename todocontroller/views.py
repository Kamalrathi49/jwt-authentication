from rest_framework.serializers import Serializer
from todocontroller.models import TodoController
from rest_framework import viewsets, permissions, status
from todocontroller.serializers import TodoSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

class TodoList(APIView):
    """
    List all Todos, or create a new Todo.
    
    """
    def get(self, request, format=None):
        user = request.user
        todos = TodoController.objects.filter(user=user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        if not user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        data['user'] = user.id
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetial(APIView):
    """
    Retrieve, update or delete a Todo instance.

    """
    def get_object(self, pk):
        try:
            return TodoController.objects.get(pk=pk)
        except TodoController.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = TodoController.objects.get(pk=pk)
        serializer = TodoSerializer(client)
        user = request.user
        if not user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = TodoSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = request.user
        if not user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

