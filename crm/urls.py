from django.urls import path
from .views import *

urlpatterns = [
    path('', first_page, name='first_page'),
    path('thank/', thanks, name='thanks')
]