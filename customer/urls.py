from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CustomerListView.as_view(), name='list'),
    path('create/', views.CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.CustomerUpdateView.as_view(), name='update'),
]
