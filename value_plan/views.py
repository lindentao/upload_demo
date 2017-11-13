import os

from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

from upload_demo.settings import MEDIA_ROOT
from .forms import UploadFileForm
from .models import UploadFile, ValuePlan

# Create your views here.


def handle_uploaded_file(f):
    with open(os.path.join(MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload(request):
    # if request.method == "POST":
    #     myFile = request.FILES.get("myfile", None)
    #     if not myFile:
    #         return HttpResponse("no files for upload!")
    #     with open(os.path.join(MEDIA_ROOT, myFile.name), 'wb+') as destination:
    #         for chunk in myFile.chunks():  # 分块写入文件
    #             destination.write(chunk)
    #     return HttpResponse("upload over!")
    # return render(request, 'upload.html')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            instance = UploadFile()
            instance.name = form.cleaned_data["name"]
            instance.file = form.cleaned_data["file"]
            instance.save()

            for line in request.FILES.get("file", None):
                list_line = line.decode().replace('\n', '').replace('"', '').split(',')
                v = ValuePlan(code=list_line[0], category=list_line[1], vehicle=list_line[2],
                              effective_date=list_line[3], effective_first=list_line[4], effective_last=list_line[5],
                              value=list_line[6], src=list_line[7])
                v.save()
            return HttpResponse("upload success!")
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
