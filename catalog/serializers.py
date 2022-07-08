# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import GeeksModel, Author
 
# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = GeeksModel
        fields = ('title', 'description')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('last_name', 'first_name')