from django.contrib import admin

# Register your models here.
from .models import Frage, Antwort	
# Register your models here.

admin.site.register(Frage)
admin.site.register(Antwort)