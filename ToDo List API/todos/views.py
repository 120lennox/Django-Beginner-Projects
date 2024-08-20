from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from .permissions import IsAuthor
from .models import Todo


# Create your views here.

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrievUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
