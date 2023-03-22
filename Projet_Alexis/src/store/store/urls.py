from django.contrib import admin
from django.urls import path
from shop.views import index, product_detail, add_to_cart, cart, delete_cart
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import signup, logout_user, login_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("login/", login_user, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", logout_user, name="logout"),
    path("cart/", cart, name="cart"),
    path("cart/delete", delete_cart, name="delete-cart"),
    path("products/<str:slug>", product_detail, name="product"),
    path("products/<str:slug>/add-to-cart", add_to_cart, name="add-to-cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # local develop server
