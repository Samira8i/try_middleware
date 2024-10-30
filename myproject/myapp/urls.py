from django.urls import path
from .views import home, another_view

urlpatterns = [
    path('', home, name='home'),
    path('another/', another_view, name='another_view'),
]
