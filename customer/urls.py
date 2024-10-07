from django.urls import path
from . import views

urlpatterns = [

    path('', views.CustomerListCreateView.as_view(), name='list-create'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),

#   개인별 가족 그룹
    path('<int:customer_pk>/family/', views.CustomerFamilyListCreateView.as_view(), name='customers-family-list-create'),
    path('<int:customer_pk>/family/<int:pk>/', views.CustomerFamilyDetailView.as_view(), name='customers-family-detail'),

#  가족 그룹별 조회
    path('family/', views.FamilyGroupListCreateView.as_view(), name='family-list-create'),
    path('family/<int:pk>/', views.FamilyDetailView.as_view(), name='family-detail'),

################################
    # 고객 리스트 HTML 페이지 렌더링
    path('list/', views.CustomerListPageView.as_view(), name='customers-list-page'),
    path('<int:pk>/detail/',views.CustomerDetailPageView.as_view(), name='customers-detail'),


]