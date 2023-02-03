from django.urls import path # This is the path function
from . import views # This is the views file


# This is the list of the routes


urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail')
]

