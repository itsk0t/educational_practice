from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DeleteView

from applications.forms import ApplicationForm


def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def application_view(request):
    current_user_id = request.user.id
    form = ApplicationForm(initial={'user_id': current_user_id})

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['files'])
            form.save()
            return HttpResponse('Заявка принята успешно')
        else:
            form = ApplicationForm()

    return render(request, 'applications/applications.html', {'form': form})


class ApplicationDeleteView(DeleteView):
    model = ApplicationForm
    # success_url = '/applications/'
    template_name = 'applications/applications_delete.html'
