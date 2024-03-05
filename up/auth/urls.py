from django.urls import path

from auth.views import RegisterUserView, LoginUserView

app_name = 'auth'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
]