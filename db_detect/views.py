from django.shortcuts import render
from django.http import HttpResponse
from .models import Db_info
# Create your views here.

# def homepage(request):
#     info = Db_info.objects.all()
#     info_list = list()
#     for db in enumerate(info):
#         info_list.append(db[0])
#         info_list.append("<br>")
#     return HttpResponse(info_list)

def insert(request):
    if request.method == "POST":
        ip = request.POST.get('ip', None)
        dbs = request.POST.get('dbs', None)
        Db_info.objects.create(ip=ip, dbs=dbs)
        Db_info.save()
    return render_to_response