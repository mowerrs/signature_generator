from django.urls import path
from .views import generate_signature

urlpatterns = [
    path("", generate_signature, name="generate_signature"),
]
