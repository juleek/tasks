from django.shortcuts import render

# from typing import List, Set, Tuple
# import typing
import typing as t

# Create your views here.

from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
