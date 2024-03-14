from django.shortcuts import render
from applications.models import Applications


def get_user_id(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        return user_id


def account_view(request):
    app_mod = Applications.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        name = request.user.first_name
        last_name = request.user.last_name
        user_id = request.user.id

    return render(request, 'account/account.html', {'username': username,
                                                    'name': name,
                                                    'last_name': last_name,
                                                    'user_id': user_id,
                                                    'app_mod': app_mod})


