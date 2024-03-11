from django.urls import path
from applications.views import application_view

app_name = 'applications'

urlpatterns = [
    path('', application_view, name='appli')
]