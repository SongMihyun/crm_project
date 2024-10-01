from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse_lazy

from counsel.forms import CounselForm
from counsel.models import Counsel
from customer.forms import CustomerForm
from customer.models import Customer
from utils.search import SearchMixin

class CustomerListView(SearchMixin,ListView):
    model = Customer
    template_name = 'customer/customer_list.html'

    # SearchMixin 으로 대체
    # def get_queryset(self):
    #     return Customer.objects.all()

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer/customer_create.html'
    form_class = CustomerForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})


class CustomerDetailView(ListView):
    model = Counsel
    template_name = 'customer/customer_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.customer = get_object_or_404(Customer, pk=self.kwargs['pk'])
        context['customer'] = self.customer
        context['counsel_form'] = CounselForm()
        return context


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer/customer_update.html'
    form_class = CustomerForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})



# 삭제기능을 구현하긴 했지만 아직 적용을 안함/
class CustomerDeleteView(DeleteView):
    model = Customer

    def get_queryset(self):
        return super().get_queryset()

    def get_success_url(self):
        return reverse_lazy('list')