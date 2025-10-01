from flights.models import Destination

destinations = [
    {"city": "Quito"},
    {"city": "Guayaquil"},
    {"city": "Bogotá"},
    {"city": "Lima"},
    {"city": "Buenos Aires"},
    {"city": "Madrid"},
    {"city": "Ciudad de México"},
    {"city": "Santiago de Chile"},
]

for data in destinations:
    Destination.objects.get_or_create(city=data["city"])
