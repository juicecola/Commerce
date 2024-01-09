
Commerce - eBay-like E-Commerce Auction Site
This project is a part of CS50W, focusing on building an eBay-like e-commerce auction site using Django. The web application allows users to post auction listings, place bids, comment on listings, and create a watchlist for their favorite items.

Prerequisites
Make sure you have watched at least Lecture 4 of CS50W before attempting this project.
Download the distribution code from this link and unzip it.
Navigate to the commerce directory in your terminal.
Getting Started
Run python manage.py makemigrations auctions to create migrations for the auctions app.
Run python manage.py migrate to apply migrations to your database.
Explore the existing codebase to understand the structure of the Django project, including URL configurations, views, and models.
Project Structure
auctions/urls.py: Defines the URL configurations for the application.
auctions/views.py: Contains views for various routes, such as login, logout, register, and index.
auctions/templates/auctions/layout.html: HTML layout of the application, with conditional rendering based on user authentication.
auctions/models.py: Defines models for the application, including User, auction listings, bids, comments, and categories.
Specifications
Models
Your application should have at least three additional models besides the User model: auction listings, bids, and comments.
Define the fields for each model based on the information you want to store.
Create Listing
Users can create a new listing with a title, description, starting bid, optional image URL, and category.
Active Listings Page
The default route displays all currently active auction listings with essential information.
Listing Page
Clicking on a listing shows detailed information.
Signed-in users can add the item to their watchlist.
Users can place bids, but they must meet certain criteria.
Watchlist
Users can view and manage their watchlist, including adding and removing listings.
Categories
Users can view a page with all listing categories.
Clicking on a category displays active listings in that category.
Additional Features
Users can add comments to listing pages.
Listing pages show comments made on the listing.
Users can close auctions they created, declaring the highest bidder as the winner.
Django Admin Interface
Administrators can use the Django admin interface to manage listings, comments, and bids.
Implementation Steps
Explore and understand the existing code.
Define models for auction listings, bids, and comments in auctions/models.py.
Implement views and templates for creating listings, displaying active listings, and viewing listing details.
Add functionality for users to add items to their watchlist and place bids.
Implement features for managing user comments on listings.
Create views and templates for the watchlist, category pages, and closed listing pages.
Utilize the Django Admin Interface for site administrators to manage listings, comments, and bids.
Additional Tips
Use the @login_required decorator to control access to certain views.
Create Django forms for various parts of the application.
Modify the CSS to customize the appearance of the website.
