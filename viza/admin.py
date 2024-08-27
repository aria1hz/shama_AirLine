from django.contrib import admin

# Register your models here.
from .models import Viza_items
from .models import single_viza


admin.site.register(Viza_items)

admin.site.register(single_viza)