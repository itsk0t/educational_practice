from django.urls import path

from documents.views import DocListView

app_name = 'documents'


urlpatterns = [
    path('doc_list', DocListView.as_view(), name='doc_list'),
]