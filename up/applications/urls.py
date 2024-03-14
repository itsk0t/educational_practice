from django.urls import path
from applications.views import application_view, ApplicationDeleteView

app_name = 'applications'

urlpatterns = [
    path('', application_view, name='appli'),
    path('<int:pk>/delete', ApplicationDeleteView.as_view(), name='app_delete'),
]