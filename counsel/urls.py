from django.urls import path
from . import views

urlpatterns = [
    path('', views.CounselListCreateView.as_view(), name='list-create'),

    path('<int:pk>/', views.CounselDetailView.as_view(), name='detail'),

    ]
