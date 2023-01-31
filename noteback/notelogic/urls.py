from django.urls import path # This is the path function
from . import views # This is the views file


# This is the list of the routes
urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/<str:pk>/', views.getNote, name='note')
]