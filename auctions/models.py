from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    product_listed = models.CharField(max_length=64, default="PRODUCT")
    product_desc = models.TextField(default="Product Description")
    product_img = models.URLField(null=True)
    init_bid = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=64, default="Misc") 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_user")
    # listing.bid.all()????

    def __str__(self):
        return f"{self.product_listed}: {self.category}"

class Bid(models.Model):
    bid = models.DecimalField(max_digits=8, decimal_places=2)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bid")
    
    def __str__(self):
        return f"{self.listing}: {self.bid}"

class Comments(models.Model):
    comment = models.TextField(max_length=400, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="listing_comments")

    def __str__(self):
        return f"{self.listing}: {self.user} - {self.comment}"