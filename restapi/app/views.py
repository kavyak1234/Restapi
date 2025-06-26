from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Todoserializers
from .models import Todo

# Create your views here.
class Todoview(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers
