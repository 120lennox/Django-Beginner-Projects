from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsAuthor

# Create your views here.
class TodoListView(generics.ListAPIView):
    #permission_classes = [IsAuthor]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthor]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
