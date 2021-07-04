from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.render_topics_of_board, name='board_topics'),
]
