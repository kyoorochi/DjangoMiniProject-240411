from django.urls import path
from .views import home_view, question_view

urlpatterns = [
    path('', home_view, name='home'),
    path('question/', question_view, name='question'),
]