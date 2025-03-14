from django.urls import path
from .views import NoteView

urlpatterns = [
    path('', NoteView.as_view(), name='notes-list'),  # The main endpoint
    path('<int:note_id>/', NoteView.as_view(), name='note-detail'),  # For GET, PUT, DELETE single note
]
