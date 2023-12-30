# myapp/urls.py
from django.urls import path
from .views import guess_number_game

urlpatterns = [
    path('guess_number_game/', guess_number_game, name='guess_number_game'),
    # Add the following line for the root path
    path('', guess_number_game, name='home'),
]
