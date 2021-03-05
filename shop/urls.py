from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='shop_add'),
    path('index/', views.index, name='shop_index'),
    path('<int:id>/edit_shop/', views.edit, name='edit_shop'),
    path('<int:id>/delete_shop/', views.delete, name='delete_shop'),
]
