# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# function based view


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
