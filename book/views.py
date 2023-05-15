from django.shortcuts import render
from django.views import generic


class Book(generic.TemplateView):
    template_name = "book.html"
    
