from django.contrib import admin
from elections.models import Loot, Election, Player, Hoard

admin.site.register(Loot)
admin.site.register(Election)
admin.site.register(Player)
admin.site.register(Hoard)
