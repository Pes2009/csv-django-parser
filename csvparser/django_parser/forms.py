from django.forms import ModelForm

from .models import ParserCsv


class UploadForm(ModelForm):
    class Meta:
        model = ParserCsv
        fields = ['upload']
