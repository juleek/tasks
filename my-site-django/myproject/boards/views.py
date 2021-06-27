from django.shortcuts import render

# from typing import List, Set, Tuple
# import typing
import typing as t

# Create your views here.

from django.http import HttpResponse
from .models import Board

def home(request):
    boards = Board.objects.all()
    boards_names: t.List[str] = []

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
