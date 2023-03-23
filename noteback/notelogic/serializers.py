from rest_framework import serializers # Import the serializer class
from .models import Note # Import the Note model



# Create a serializer class
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Note
        fields = ['id', 'title', 'cover_image', 'body', 'created', 'updated']







