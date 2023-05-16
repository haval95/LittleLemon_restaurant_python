from django.urls import path
from .views import BookV


urlpatterns = [
    path("", BookV, name="book_view")
]
