from django.urls import path
from . import views
from .views import search_product

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),

    path('process_order/', views.processOrder, name="process_order"),

    path('login/', views.login_page, name="login"),

    path('logout/', views.logout_view, name="logout"),

    path('search/', views.search_product, name="search"),

    path('<int:product_id>/', views.product_detail, name='product_detail'),
]