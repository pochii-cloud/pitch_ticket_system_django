from django.contrib import admin

# Register your models here.
from core.models import Field, Team, Fixture, Contact

admin.site.register(Field)
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Contact)
