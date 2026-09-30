# 

from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    # Authentication
    path(
        'signup/',
        views.signup_view,
        name='signup'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # E-Card CRUD
    path(
        'cards/',
        views.card_list,
        name='card_list'
    ),

    path(
        'cards/<int:pk>/',
        views.card_detail,
        name='card_detail'
    ),

    path(
        'cards/create/',
        views.card_create,
        name='card_create'
    ),

    path(
        'cards/<int:pk>/edit/',
        views.card_update,
        name='card_update'
    ),

    path(
        'cards/<int:pk>/delete/',
        views.card_delete,
        name='card_delete'
    ),
]