from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', BookList.as_view(), name='listBook'),
    path('book/newBook/', NewBook.as_view(), name='newBook'),
    path('book/detailBook/<int:pk>', DetailBook.as_view(), name='detailBook'),
]