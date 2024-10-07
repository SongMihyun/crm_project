
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

#     customer
    path('customer/', include('customer.urls')),

#     counsel
    path('customer/<int:customer_pk>/counsel/', include('counsel.urls')),
]
