from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note



# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/users/',
        '/api/users/login/',
        '/api/users/register/',
        '/api/users/profile/',
        '/api/users/profile/update/',
        '/api/users/profile/delete/',
        '/api/notes/',
        '/api/notes/create/',
        '/api/notes/<str:pk>/update/',
        '/api/notes/<str:pk>/delete/',
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)



