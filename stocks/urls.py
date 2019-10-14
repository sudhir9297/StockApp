from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('stock',views.add_stock, name='stock' ),
    path('delete/<stock_id>',views.delete, name='delete' ),
]
