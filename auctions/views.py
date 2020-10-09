from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listings, Bid, Comments
from .forms import ListingsForm

# Adding the @login_required decorator on top of any view will ensure that only a user who is logged in can access that view.

def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    
    form = ListingsForm()

    if request.method == "POST":
        form = ListingsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, "auctions/create.html", context)



        # user = request.user
        # product_listed = request.POST.get("title")
        # product_desc = request.POST.get("description")
        # product_img = request.POST.get("image")
        # init_bid = float(request.POST.get("initial_bid"))
        # category = request.POST.get("category")

        # listings = Listings(user = user, product_listed = product_listed, product_desc = product_desc, 
        #                     product_img = product_img, init_bid = init_bid, category = category)
        # listings.save()
