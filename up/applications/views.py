from django.http import HttpResponse
from django.shortcuts import render
from applications.forms import ApplicationForm


def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
            form.save()
            return HttpResponse('Заявка принята успешно')
        else:
            form = ApplicationForm()

        return render(request, 'applications/applications.html', {'form': form})
