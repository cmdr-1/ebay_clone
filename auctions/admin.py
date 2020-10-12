from django.contrib import admin
from .models import User, Listings, Bid, Comments

# Register your models here.

admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Comments)