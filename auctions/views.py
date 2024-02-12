from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Listing
from .forms import ListingForm
from .models import User, Watchlist
from django.contrib.auth import get_user


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


@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            starting_bid = form.cleaned_data['starting_bid']
            category = form.cleaned_data['category']
            image_url = form.cleaned_data['image_url']

            # Create new listing object
            new_listing = Listing(
                title=title,
                description=description,
                starting_bid=starting_bid,
                category=category,
                image_url=image_url,
                current_bid=starting_bid,  # Set initial bid as starting bid
                created_by=request.user
            )
            new_listing.save()
            return redirect('index')
    else:
        form = ListingForm()

    return render(request, 'auctions/create_listing.html', {'form': form})


def active_listings(request):
    active_listings = Listing.objects.all()
    return render(request, 'auctions/active_listings.html', {'active_listings': active_listings})


@login_required
def watchlist(request):
    user = get_user(request)
    user_watchlist = Watchlist.objects.filter(user=request.user)
    return render(request, 'auctions/watchlist.html', {'watchlist': user_watchlist})
