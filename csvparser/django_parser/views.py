import csv

from django.shortcuts import render

from .models import CsvList
from .forms import UploadForm


def upload(request, *args, **kwargs):
    form = UploadForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=True)
            reader = csv.DictReader(instance.upload.file)
            for row in reader:
                parsing, created = CsvList.objects.get_or_create(
                    id=row['id'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    domain=row['domain'],
                    url=row['url']
                )

    context = {
        "form": form,
    }
    return render(request, "django_parser/upload.html", context, )


def list(request):
    queryset = CsvList.objects.order_by('id')
    context = {
        "queryset": queryset,
    }
    return render(request, "django_parser/list.html", context, )
