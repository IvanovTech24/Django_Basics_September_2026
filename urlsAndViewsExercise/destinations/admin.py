from django.contrib import admin
from destinations.models import Destination


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    ...
