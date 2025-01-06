from django.urls import path
from . import views

urlpatterns = [
    path('test/<int:id>/', views.api_view, name='update_book'),
]
