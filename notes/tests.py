from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Note

class NoteAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note_data = {"title": "Test Note", "content": "This is a test note."}
        self.note = Note.objects.create(title="Existing Note", content="Already exists.")

    def test_get_all_notes(self):
        response = self.client.get("/api/notes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_note(self):
        response = self.client.get(f"/api/notes/{self.note.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.note.title)

    def test_create_note(self):
        response = self.client.post("/api/notes/", self.note_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.note_data["title"])

    def test_update_note(self):
        updated_data = {"title": "Updated Note", "content": "Updated content."}
        response = self.client.put(f"/api/notes/{self.note.id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], updated_data["title"])

    def test_delete_note(self):
        response = self.client.delete(f"/api/notes/{self.note.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
