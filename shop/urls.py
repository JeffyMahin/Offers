from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='shop_add'),
    path('index/', views.index, name='shop_index')
]
