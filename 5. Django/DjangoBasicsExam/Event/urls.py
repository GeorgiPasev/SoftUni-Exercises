from django.urls import path

from Event import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events_list, name='events_list'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:pk>/details/', views.event_details, name='event_details'),
    path('events/<int:pk>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:pk>/delete/', views.delete_event, name='delete_event'),
]