from django.urls import path

from Organizer import views

urlpatterns = [
    path('create/', views.create_organizer, name='create_organizer'),
    path('details/', views.organizer_details, name='organizer_details'),
    path('edit/', views.edit_organizer, name='edit_organizer'),
    path('delete/', views.delete_organizer, name='delete_organizer'),
]