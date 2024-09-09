from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from note_api.serializers import NoteSerializer
from rest_framework import status


SerializerValidationFailureResponse = inline_serializer(
    name='ErrorResponse',
    fields={
        'errors': serializers.ListField(
            child=serializers.CharField(),
            help_text='List of error messages describing why the request was invalid.'
        )
    }
)

def create_note_schema():
    return extend_schema(
        summary='Create Note',
        description='This API allows you to create a note by providing the title and body of the note.',
        tags=['Notes'],
        responses={
            201: NoteSerializer,
            400: SerializerValidationFailureResponse,
            404: status.HTTP_404_NOT_FOUND
        }
    )

def get_notes_schema():
    return extend_schema(
        summary='Get Notes',
        description='This API allows you to retrieve all notes.',
        tags=['Notes'],
        responses={
            200: NoteSerializer,    # For getting a note by ID
            404: 'No note found with the given ID.',
            200: NoteSerializer(many=True)  # For getting all notes
        }
    )

def update_note_schema():
    return extend_schema(
        summary='Update Note',
        description='This API allows you to update a note by its ID.',
        tags=['Notes'],
        responses={
            400: SerializerValidationFailureResponse,
            200: NoteSerializer
        }
    )


def query_note_by_title_schema():
    return extend_schema(
        summary='Query Note By Title',
        description='This API allows you to query notes by their title.',
        tags=['Notes'],
        request=None,
        responses={
            200: NoteSerializer(many=True),
            404: 'No notes found with the given title.'
        },
    )