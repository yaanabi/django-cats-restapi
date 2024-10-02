from django.contrib import admin
from .models import Cat, CatRating, Breed
# Register your models here.


admin.site.register(Cat)
admin.site.register(CatRating)
admin.site.register(Breed)