from rest_framework.response import Response
from rest_framework.decorators import api_view
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


