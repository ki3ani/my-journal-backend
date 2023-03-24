from django.urls import path # This is the path function
from . import views # This is the views file
from rest_framework_simplejwt.views import TokenRefreshView # This is the TokenRefreshView function




# This is the list of the routes


urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),

]

