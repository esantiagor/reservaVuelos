from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from datetime import timedelta
from .models import FlightRequest

@shared_task
def send_flight_reminders():
    today = timezone.now().date()
    reminder_date = today + timedelta(days=2)
    flights = FlightRequest.objects.filter(travel_date=reminder_date)
    for flight in flights:
        send_mail(
            subject='Upcoming Flight Reminder',
            message=f'Your flight to {flight.destination} is in 2 days!',
            from_email='noreply@flights.com',
            recipient_list='nodestination@flights.com', #aqui email de user
        )
