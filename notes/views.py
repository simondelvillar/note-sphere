from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

class NoteView(APIView):
    def get(self, request, note_id=None):
        if note_id:
            try:
                note = Note.objects.get(id=note_id)
                serializer = NoteSerializer(note)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Note.DoesNotExist:
                return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            notes = Note.objects.all()
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, note_id):
        try:
            note = Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id):
        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return Response({'message': 'Note deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Note.DoesNotExist:
            return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
