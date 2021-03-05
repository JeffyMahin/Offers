from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='offer_add'),
    path('index/', views.index, name='offer_index'),
    path('offer_detail/<int:id>/', views.offer_detail_view, name='offer_detail'),
    path('pending/', views.offer_pending, name='offer_pending'),
    path('<int:offer_id>/accept_offer/', views.accept_offer, name='accept_offer'),
    path('<int:offer_id>/delete_offer/', views.delete_offer, name='delete_offer')
]
