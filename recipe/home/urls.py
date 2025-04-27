from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('update/<int:recipe_id>/', views.update_recipe, name='update_recipe'),
]