from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todocontroller.views import TodoList, TodoDetial

urlpatterns = [
    path('todos/', TodoList.as_view()),
    path('todo/<int:pk>/', TodoDetial.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

