import shopifyapi
from django.shortcuts import render
from .models import ShopifyUser


def retrieve_shopify_users(request):
    # Connect to Shopify API
    shopify = shopifyapi.init()

    # Retrieve users from Shopify
    users = shopify.get_users()

    # Update or create ShopifyUser objects in the database
    for user in users:
        shopify_user, _ = ShopifyUser.objects.get_or_create(shopify_id=user["id"])
        shopify_user.name = user["name"]
        shopify_user.email = user["email"]
        shopify_user.save()

    # Render a template or return a response
    return render(request, "shopify_integration/users.html", {"users": users})
