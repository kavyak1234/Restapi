from rest_framework import serializers
from .models import Todo

class Todoserializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        field = '__all__'
