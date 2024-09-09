from django.shortcuts import render, get_object_or_404
from note_api.serializers import NoteSerializer
from note_api.models import Note
from rest_framework import views, status
from rest_framework.response import Response


# Create your views here.

class NoteList(views.APIView):
    # Fetch all notes and note by id
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                note = Note.objects.get(pk=pk)
                serializer = NoteSerializer(note)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Note.DoesNotExist:
                return Response({'error': 'No note found with the given ID.'}, status=status.HTTP_404_NOT_FOUND)
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create a new note
    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Update a note
    def put(self, request, pk, format=None):
        note = Note.objects.filter(id=pk).first()
        if not note:
            return Response({'error': 'No note found with the given ID.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Query notes by title
class QueryNoteListByTitle(views.APIView):
    def get(self, request, format=None):
        # import pdb; pdb.set_trace()
        title = request.query_params.get('title', None)
        if title:
            notes = Note.objects.filter(title__icontains=title)
            if not notes.exists():
                return Response({'error': 'No notes found with the given title.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'title parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
