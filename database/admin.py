from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ArtWork)
admin.site.register(Artist)
admin.site.register(Invoice)
admin.site.register(Purchaser)