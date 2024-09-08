from django.urls import path
from booking import views

urlpatterns = [
    path('rooms/', views.room_list, name="room-list"),
    path('booking/', views.book_room, name="book-room")
]