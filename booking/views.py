from django.shortcuts import render, redirect
from .models import Room, Booking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

# Create your views here.

class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'booking/room_list.html'

class RoomDetailsView(DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'booking/room_detail.html'

@login_required
def book_room(request, pk=None):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(number=room_number)
        except Room.DoesNotExist:
            return HttpResponse("Room not found!", status=400)

        if pk:  
            try:
                booking = Booking.objects.get(id=pk, user=request.user)  
                booking.room = room
                booking.start_time = start_time
                booking.end_time = end_time
                booking.save()
            except Booking.DoesNotExist:
                return HttpResponse("Booking not found!", status=404)
        else: 
            booking = Booking.objects.create(
                user=request.user,
                room=room,
                start_time=start_time,
                end_time=end_time
            )

        return redirect("booking-detail", pk=booking.id)
    else:
        if pk:
            try:
                booking = Booking.objects.get(id=pk, user=request.user)
            except Booking.DoesNotExist:
                return HttpResponse("Booking not found!", status=404)
        else:
            booking = None

        return render(request, "booking/booking_form.html", {"booking": booking})

def delete_booking(request, pk):
    booking = Booking.objects.filter(id=pk).delete()
    return redirect("user-bookings")



def booking_detail(request, pk):
    booking = Booking.objects.get(id=pk)

    context = {
        "booking": booking
    }

    return render(request, "booking/booking_detail.html", context)

def user_booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    print(bookings)

    context = {
        "bookings": bookings
    }

    return render(request, "booking/user_bookings.html", context)