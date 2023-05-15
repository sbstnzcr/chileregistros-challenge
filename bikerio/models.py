from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Network(models.Model):
    company = models.ManyToManyField(Company)
    gbfs_href = models.URLField()
    href = models.CharField(max_length=100)
    network_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Station(models.Model):
    network = models.ForeignKey(
        Network, on_delete=models.CASCADE, related_name="stations"
    )
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    station_id = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Extra(models.Model):
    station = models.OneToOneField(Station, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    altitude = models.IntegerField(null=True)
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment = models.ManyToManyField(Payment)
    payment_terminal = models.BooleanField()
    renting = models.BooleanField()
    returning = models.BooleanField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=100)
