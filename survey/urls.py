from django.urls import path
from .views import home_view, question_view, over_view, result_view

urlpatterns = [
    path('', home_view, name='home'),
    path('question/', question_view, name='question'),
    path('over/', over_view, name='over'),
    path('result/', result_view, name='result'),
]