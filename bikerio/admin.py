from django.contrib import admin

from bikerio.models import Company, Extra, Network, Payment, Station

# Register your models here.
admin.site.register(Company)
admin.site.register(Network)
admin.site.register(Station)
admin.site.register(Payment)
admin.site.register(Extra)
