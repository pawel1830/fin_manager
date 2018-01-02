# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Transactions, Wallets
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.views.generic.edit import DeleteView, UpdateView
from forms import WalletForm
# Create your views here.
from django.http import HttpResponse
import json
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
import logging
from django.template import RequestContext
# Get an instance of a logger
logger = logging.getLogger(__name__)
class HomePageView(TemplateView):

    template_name = "dashboard.html"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        return super(HomePageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        wallets = Wallets.objects.filter(owner=self.request.user.username)
        context['transactions'] = Transactions.objects.filter(wallet_id__in=wallets).order_by('-date')[:10]
        return context


class NewWalletView(FormView):
    template_name = "wallets.html"
    form_class = WalletForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewWalletView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("index")
class DeleteWalletView(DeleteView):
    model = Wallets
    template_name = "wallets_confirm_delete.html"
    success_url = reverse_lazy('index')
    def get_object(self, *args, **kwargs):
        wallet_del = get_object_or_404(Wallets, name=self.kwargs['pk'])

        return wallet_del

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        resp = super(DeleteWalletView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
class EditWallet(UpdateView):
    model = Wallets
    form_class = WalletForm
    template_name = "wallets.html"

    def get_object(self, *args, **kwargs):
        wallets = get_object_or_404(Wallets, name=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return wallets

    def get_success_url(self, *args, **kwargs):
        return reverse("index")
class WalletDetailView(DetailView):
    model = Wallets
    template_name = 'wallet_detail.html'

    def get_object(self):
        return get_object_or_404(Wallets, name=self.kwargs['name'])
class UserView(TemplateView):
    template_name = 'user_detail.html'