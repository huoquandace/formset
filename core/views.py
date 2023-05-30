from django.shortcuts import render
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *


class ParentList(ListView):
    model = Parent


class ParentCreate(CreateView):
    model = Parent
    fields = ['name']
    success_url = reverse_lazy('parents-list')

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.POST:
            context['children'] = ChildrenFormset(self.request.POST)
        else:
            context['children'] = ChildrenFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        children = context['children']
        with transaction.atomic():
            self.object = form.save()
            if children.is_valid():
                children.instance = self.object
                children.save()
        return super().form_valid(form)