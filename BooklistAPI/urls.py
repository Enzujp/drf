from django.urls import path
from . import views 

urlpatterns = [
    path('books/', views.books, name="books"),
    path('orders', views.Orders.listOrders, name="orders"),
    # path('books/<int:pk>', views.BookView.as_view, name="bookview")
]