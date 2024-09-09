from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from note_api.models import Note
from note_api.serializers import NoteSerializer


# Create your tests here.
class NoteTests(APITestCase):
    def setUp(self):
        self.note1 = Note.objects.create(title='Note 1', body='Body of Note 1')
        self.note2 = Note.objects.create(title='Note 2', body='Body of Note 2')

    def test_create_note(self):
        url = reverse('notes')
        data = {'title': 'New Note', 'body': 'Body of New Note'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 3)
        self.assertEqual(Note.objects.latest('id').title, 'New Note')

    def test_get_all_notes(self):
        url = reverse('notes')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_note_by_id(self):
        url = reverse('notes', args=[self.note1.pk])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Note 1')

    def test_update_note(self):
        url = reverse('notes', args=[self.note1.pk])
        data = {'title': 'Updated Note 1', 'body': 'Updated Body of Note 1'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get(pk=self.note1.pk).title, 'Updated Note 1')

    def test_query_notes_by_title(self):
        url = reverse('note-query') + '?title=Note 1'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Note 1')

    def test_query_notes_by_title_not_found(self):
        url = reverse('note-query') + '?title=Nonexistent'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'No notes found with the given title.')

    def test_query_notes_by_title_missing_parameter(self):
        url = reverse('note-query')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'title parameter is required.')