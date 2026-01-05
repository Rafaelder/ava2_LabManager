from django.contrib import admin
from .models import Laboratorio, Equipamento, Reserva

admin.site.register(Laboratorio)
admin.site.register(Equipamento)
admin.site.register(Reserva)