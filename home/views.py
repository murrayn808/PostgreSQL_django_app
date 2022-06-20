from django.shortcuts import render
from django.views import generic
from .models import Greeting

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'home_page'
    def get_queryset(self):
        """Return the all greetings."""
        return Greeting.objects.all()