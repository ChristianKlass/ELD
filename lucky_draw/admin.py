from django.contrib import admin
from .models import Contestant, Draw, Event, Prize

# Register your models here.
admin.site.register(Contestant)
admin.site.register(Draw)
admin.site.register(Event)
admin.site.register(Prize)
