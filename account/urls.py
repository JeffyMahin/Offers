from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registration, name='user_registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin_user_index/', views.admin_user_index, name='admin_user_index'),
    path('shopkeeper_user_index/', views.shopkeeper_user_index, name='shopkeeper_user_index'),
    # path('delete_admin/<int:id>/', views.delete_admin, name='delete_admin')
]
