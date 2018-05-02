from django.urls import path
from .views import get_algos

urlpatterns = [
    path('', get_algos, name = "CompleteApp"),
]
