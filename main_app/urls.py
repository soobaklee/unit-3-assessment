from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('items/create/', views.WishCreate.as_view(), name='wish_create'),
    # path('/<int:pk>/delete/', views.WishDelete.as_view(), name='wish_delete'),
]