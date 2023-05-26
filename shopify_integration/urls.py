from django.urls import path
from shopify_integration.views import retrieve_shopify_users

urlpatterns = [
    # Other URL patterns
    path('shopify/users/', retrieve_shopify_users, name='retrieve_shopify_users'),
]
