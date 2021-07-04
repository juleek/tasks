# from django.shortcuts import render

# from typing import List, Set, Tuple
# import typing
import typing as t

# Create your views here.

import django.shortcuts as helpers
from . import models as mdl

def home(request):
    boards = mdl.Board.objects.all()
    return helpers.render(request, 'home.html', {'boards': boards})

def render_topics_of_board(request, pk):
    # helpers.get_object_or_404
    return helpers.render(request, 'topics.html', {'board': board})
