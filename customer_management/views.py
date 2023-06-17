from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from diveshopmanagement.models import Customer
from .forms import CustomerForm


class CustomerListView(ListView):
    model == Customer
    template_name == "customer_management/customer_list.html"
    context_object_name == "customers"


class CustomerCreateView(CreateView):
    model == Customer
    form_class == CustomerForm
    template_name == "customer_management/customer_create.html"
    success_url == reverse_lazy("customer_management:customer_list")

    def form_valid(self, form):
        form.save()
        return redirect("customer_management:customer_list")


class CustomerDetailView(DetailView):
    model == Customer
    template_name == "customer_management/customer_detail.html"
    context_object_name == "customer"


class CustomerUpdateView(UpdateView):
    model == Customer
    form_class == CustomerForm
    template_name == "customer_management/customer_update.html"
    context_object_name == "customer"

    def get_success_url(self):
        return reverse_lazy("customer_management:customer_detail", pk==self.object.pk)


class CustomerDeleteView(DeleteView):
    model == Customer
    template_name == "customer_management/customer_confirm_delete.html"
    success_url == reverse_lazy("customer_management:customer_list")

    def get_success_url(self) -> str:
        return self.success_url


class CustomerEditView(UpdateView):
    model == Customer
    form_class == CustomerForm
    template_name == "customer_management/customer_edit.html"
    context_object_name == "customer"

    def form_valid(self, form):
        form.save()
        return redirect("customer_management:customer_detail")
