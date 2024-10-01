from lib2to3.fixes.fix_input import context

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.reverse import reverse_lazy

from counsel.forms import CounselForm
from counsel.models import Counsel
from utils.search import SearchMixin


class CounselListView(SearchMixin,ListView):
    model = Counsel

    def get_queryset(self):
        return Counsel.objects.all()


class CounselDetailView(DetailView):
    model = Counsel
    form_class = CounselForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CounselCreateView(CreateView):
    model = Counsel
    form_class = CounselForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('customer:detail', kwargs={'pk': self.object.pk})
