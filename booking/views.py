from django.shortcuts import render, redirect
from .models import Room, Booking
from django.http import HttpResponse

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()

    context = {
        "rooms": rooms
    }

    return render(request, "booking/room_list.html", context)

def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse("Wrong room number!", status_code=400)
        
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )

        return redirect("booking-detail", pk=booking.id)
    else:
        return render(request, template_name="booking/booking_form.html")


def booking_detail(request, pk):
    booking = Booking.objects.get(id=pk)

    context = {
        "booking": booking
    }

    return render(request, "booking/booking_detail.html", context)