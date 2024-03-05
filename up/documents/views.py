from django.shortcuts import render
from django.views.generic import ListView, DetailView

from documents.models import Documents


class DocListView(ListView):
    model = Documents
    template_name = 'documents/doc_list.html'
    context_object_name = 'doc_list'


class DocDetailView(DetailView):
    model = Documents
    template_name = 'documents/doc_detail.html'
    context_object_name = 'doc_detail'
