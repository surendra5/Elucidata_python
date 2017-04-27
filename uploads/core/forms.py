from django import forms

from uploads.core.models import Document
from uploads.core.handleFile import process_file

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )
