from django.urls import path
from .views import get_algos, predictScore

urlpatterns = [
    path('', get_algos, name = "CompleteApp"),
    path('predictScore', predictScore, name = "predictScore"),
]
