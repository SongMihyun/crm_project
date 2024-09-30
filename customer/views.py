from django.shortcuts import render
from django.views.generic import ListView

from customer.models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'

    def get_queryset(self):
        # 슈퍼유저일 경우 모든 고객 리스트를 반환
        if self.request.user.is_superuser:
            return Customer.objects.all()
        else:
            # 일반 사용자일 경우 일부 고객 리스트를 필터링하여 반환
            return Customer.objects.filter(assigned_user=self.request.user)