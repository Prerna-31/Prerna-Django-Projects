from django.urls import path
from . import views

## urlPatterns is a list of paths.
## path has 3 arguments. 1. url   2.Function     3.webpage name which will be shown in webpage url.

urlpatterns = [
    path('',views.index, name='index.html')
]