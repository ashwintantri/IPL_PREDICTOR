from django.urls import path
from .views import get_algos, predictScore, predictWinner

urlpatterns = [
    path('', get_algos, name = "CompleteApp"),
    path('predictScore', predictScore, name = "predictScore"),
    path('predictWinner', predictWinner, name = "predictWinner")
]
