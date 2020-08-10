from django.urls import path
from .views import ListQuestions

urlpatterns = [
    path('', ListQuestions.as_view())
]
