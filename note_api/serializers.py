from rest_framework import serializers
from note_api.models import Note

# Create your serializers here.
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'