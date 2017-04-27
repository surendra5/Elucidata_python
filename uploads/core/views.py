from django.http import HttpResponse
from django.shortcuts import render

from uploads.core.forms import DocumentForm
from uploads.core.handleFile import process_file
from uploads.core.models import Document


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })




def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
        # call to the new method
        csv = process_file(document.document)
        response = HttpResponse(csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=result.csv'
        return response
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

