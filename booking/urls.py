from django.urls import path
from booking import views

urlpatterns = [
    path('', views.room_list, name="room-list"),
    path('booking/', views.book_room, name="book-room"),
    path('booking-detail/<int:pk>', views.booking_detail, name="booking-detail"),
    path('user-bookings/', views.user_booking_list, name="user-bookings"),
]