import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()


from datetime import datetime

import requests

from bikerio.models import Company, Extra, Network, Payment, Station

URL = "https://api.citybik.es/v2/networks/bikerio"

response = requests.get(URL)
data = response.json()

network_data = data["network"]
companies_data = network_data["company"]

companies = []
for company_name in companies_data:
    company, _ = Company.objects.get_or_create(name=company_name)
    companies.append(company)

network = Network.objects.create(
    name=network_data["name"],
    gbfs_href=network_data["gbfs_href"],
    href=network_data["href"],
    network_id=network_data["id"],
    city=network_data["location"]["city"],
    country=network_data["location"]["country"],
    latitude=network_data["location"]["latitude"],
    longitude=network_data["location"]["longitude"],
)
network.company.set(companies)


stations_data = network_data["stations"]
for station_data in stations_data:
    try:
        timestamp = datetime.strptime(station_data["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        timestamp = datetime.strptime(station_data["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
    station = Station.objects.create(
        network=network,
        empty_slots=station_data["empty_slots"],
        free_bikes=station_data["free_bikes"],
        station_id=station_data["id"],
        latitude=station_data["latitude"],
        longitude=station_data["longitude"],
        name=station_data["name"],
        timestamp=timestamp,
    )

    extra_data = station_data["extra"]
    payments_data = extra_data["payment"]

    payments = []
    for payment_name in payments_data:
        payment, _ = Payment.objects.get_or_create(name=payment_name)
        payments.append(payment)

    extra = Extra.objects.create(
        station=station,
        address=extra_data["address"],
        altitude=extra_data["altitude"],
        ebikes=extra_data["ebikes"],
        has_ebikes=extra_data["has_ebikes"],
        last_updated=extra_data["last_updated"],
        normal_bikes=extra_data["normal_bikes"],
        payment_terminal=extra_data["payment-terminal"],
        renting=extra_data["renting"],
        returning=extra_data["returning"],
        slots=extra_data["slots"],
        uid=extra_data["uid"],
    )
    extra.payment.set(payments)
