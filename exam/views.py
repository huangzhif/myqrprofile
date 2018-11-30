from django.shortcuts import render, HttpResponse
from .models import ExamModel
from MyQR import myqr
import time
import os
from .forms import ExamForm


# Create your views here.


def index(request):
    if request.method == 'GET':
        form = ExamForm(initial={"contrast":1.0,"brightness":1.0})
        # print(form)
        return render(request, "exam.html", {"form": form})
    elif request.method == 'POST':
        try:
            form = ExamForm(request.POST, request.FILES)
            # print(request.POST)
            # print(type(request.FILES["qrpic"]))
            # print(request.FILES["qrpic"])
            form.save()

            filename, tailname = os.path.splitext(str(request.FILES["qrpic"]))
            # print(str(request.FILES["qrpic"])[-4:])
            if str(request.FILES["qrpic"])[-4:].upper() in ['.JPG','.JPEG']:
                pro = '.png'
            else:
                pro = tailname

            import uuid
            newname = uuid.uuid1()
            contrast = float(10.0) if float(request.POST["contrast"]) > 10 else float(request.POST["contrast"])
            brightness = float(10.0) if float(request.POST["brightness"]) > 10 else float(request.POST["brightness"])
            # print(filename,pro,sep='-')
            myqr.run(words=request.POST['remark'],
                     version=8,
                     level='H',
                     contrast=contrast,
                     brightness=brightness,
                     picture='/home/vagrant/4love/mysite/media/output/qrpic/'+ str(request.FILES["qrpic"]),
                     colorized=True,
                     save_name= '/home/vagrant/4love/mysite/media/output/' + str(newname) + pro,
                     save_dir='/home/vagrant/4love/mysite')
            return render(request, "exam.html", {"form": form,"img":'/media/output/' + str(newname) + pro})
        except Exception as e:
            return HttpResponse(e)
