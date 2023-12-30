# myapp/views.py
from django.shortcuts import render

def guess_number_game(request):
    return render(request, 'myapp/guess_number_game.html')
