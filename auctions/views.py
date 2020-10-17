from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listings, Bid, Comments, Watchlist
from .forms import ListingsForm, CommentForm

# Adding the @login_required decorator on top of any view will ensure that only a user who is logged in can access that view.

def index(request):
    queryset = Listings.objects.all()
    context = {
        'object_list': queryset
    }

    return render(request, "auctions/index.html", context)


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
    
    form = ListingsForm(request.POST or None)  
    if form.is_valid():
        form.instance.listing_user = request.user
        form.save()
        form = ListingsForm()

    context = {
        'form': form
    }
    return render(request, "auctions/create.html", context)

def listing(request, id):

    # obj = Listings.objects.get(id=id)
    listing = Listings.objects.get(id=id)
    comments = listing.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            new_comment = comment_form.save(commit=False)
            new_comment.listing = listing
            new_comment.save()
    else:
        comment_form = CommentForm()

    # find a way to check if the listing is being watched
    # provide context like 'watching': True'

    
    context = {
        'listing': listing,
        'comments': comments,
        "new_comment": new_comment,
        "comment_form": comment_form
    }

    return render(request, "auctions/listing.html", context)

def addwatchlist(request, id):

    listing = Listings.objects.get(id=id)
    print(listing)
    user = request.user
    watched = Watchlist(listing = listing, user = user)
    watched.save()
    return HttpResponseRedirect(reverse('listing', args=(listing.id,)))

def watchlist(request):
    
    queryset = Watchlist.objects.filter(user=request.user)
    wlisting = Listings.objects.all()

    context = {
        'watchlist': queryset,
        'wlisting': wlisting
    }

    return render(request, "auctions/watchlist.html", context)    

# def makebid(request, bid):
    
#     if int(new_bid) > (current_bid) and int(new_bid) > 0:
#         message = "Your bid has been accepted"
#         print(f"Cheecking 1: {message}")
#         messagebid = f"The Current Bid is $ {new_bid}"
#         print(f"Checking 2 {messagebid}")
#         bidding = Bid(listing = listing, bid = new_bid, bidder = user)
#         bidding.save()
#     else:
#         error = "Your bid must be larger than the current bid"
#         print(f"Checking 3 : {error}")

#     return HttpResponseRedirect(reverse('listing', args=(listing_id,)))