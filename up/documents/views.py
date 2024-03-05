from django.shortcuts import render
from django.views.generic import ListView

from documents.models import Documents


class DocListView(ListView):
    model = Documents
    template_name = 'documents/doc_list.html'
    context_object_name = 'doc_list'