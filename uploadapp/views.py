from django.shortcuts import render
from uploadapp.forms import UploadForm


def upload_image(request):
    form = UploadForm()
    return render(request, 'uploadapp/add_image.html', {'form': form})
