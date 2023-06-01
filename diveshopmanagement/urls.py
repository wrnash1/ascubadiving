from django.contrib import admin
from django.urls import include, path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", accounts_views.home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("airfills/", include("airfills.urls")),
    path("customer_management/", include("customer_management.urls")),
    path("tanks/", include("tanks.urls")),
    path("compressor/", include(compressor_urls)),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
]
