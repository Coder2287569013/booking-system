from django.urls import path
from booking import views

urlpatterns = [
    path('', views.RoomListView.as_view(), name="room-list"),
    path('booking/', views.book_room, name="book-room"),
    path('booking/<int:pk>', views.book_room, name="update-book"),
    path('booking-detail/<int:pk>', views.booking_detail, name="booking-detail"),
    path('booking-delete/<int:pk>', views.delete_booking, name="booking-delete"),
    path('user-bookings/', views.user_booking_list, name="user-bookings"),
    path('room-detail/<int:pk>', views.RoomDetailsView.as_view(), name="room-detail"),
]