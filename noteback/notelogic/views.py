from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote
# Create your views here.


#This view will return the routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/notes/',
        '/api/notes/<str:pk>/'
    ]
    return Response(routes)

# This view will return the notes list
@api_view(['GET', 'POST'])
def getNotes(request):

    # If the request is a GET request
    if request.method == 'GET':
        return getNotesList(request)

    # If the request is a POST request
    if request.method == 'POST':
        return createNote(request)

# This view will return the note detail
@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):


    # If the request is a GET request
    if request.method == 'GET':
        return getNoteDetail(request, pk)

    # If the request is a PUT request
    if request.method == 'PUT':
        return updateNote(request, pk)

    # If the request is a DELETE request
    if request.method == 'DELETE':
        return deleteNote(request, pk)
