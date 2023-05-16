from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name="menu_view"),
    path("<int:id>/", views.detail, name="detail_view"),
    
]
