from django.contrib import admin
from .models import Pair
from .forms import PairForm


class PairAdmin(admin.ModelAdmin):

    model = Pair
    form = PairForm


admin.site.register(Pair, PairAdmin)
