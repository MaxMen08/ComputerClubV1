from django.contrib import admin
from .models import Player, Hall, Computers, Visit

# Register your models here.
admin.site.register(Player)
admin.site.register(Hall)
admin.site.register(Computers)
admin.site.register(Visit)
