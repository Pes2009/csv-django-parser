from django.shortcuts import render

from .forms import UploadForm
from .models import CsvList

import csv


# Create your views here.


def upload(request, *args, **kwargs):
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=True)

    if request.method == "POST":
        cs = request.FILES.get("upload")
        path = str(cs)
        directory = "C:\\Users\\martin\\Desktop\\test\\csv-django-parser\\csvparser\\media_cdn\\"

        with open(str(directory) + str(path)) as csvfile:
            reader = csv.DictReader(csvfile)
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
