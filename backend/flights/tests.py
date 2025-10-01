from django.test import TestCase
from django.contrib.auth.models import User
from .models import FlightRequest, Destination
from datetime import date

class FlightRequestTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.dest = Destination.objects.create(city='Quito')
    
    def test_create_flight_request(self):
        flight = FlightRequest.objects.create(user=self.user, destination=self.dest, travel_date=date.today())
        self.assertEqual(flight.status, 'PENDING')
        self.assertEqual(flight.destination.city, 'Quito')
