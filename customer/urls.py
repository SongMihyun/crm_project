from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CustomerListView.as_view(), name='list'),
]
