from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.create_short_url, name='create_short_url'),
    path('links/', views.link_list, name='link_list'),
    path('<str:short_code>/', views.redirect_short_url, name='redirect_short_url'),
]
