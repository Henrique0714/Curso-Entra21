from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos),
    path('teclados/', views.teclados),
    path('mouses/', views.mouses),
    path('headsets/', views.headsets),
]