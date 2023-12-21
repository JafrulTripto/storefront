from django.urls import path

from playground.views import hello_world

urlpatterns = [
    path('hello/', hello_world)
]
