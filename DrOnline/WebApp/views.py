from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from WebApp import forms
from WebApp.models import OnlineOp
import csv
import datetime
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def Home(request):
    return render(request,"MyApp/Home.html")
def Details(request):
    date=datetime.datetime.now()
    dic={"dt_now":date}
    return render(request,"MyApp/Details.html",dic)
def Success(request):
    return render(request,'MyApp/Success.html')
def Final(request):
    flist=OnlineOp.objects.all()
    return render(request,'MyApp/Final.html',{'flist':flist})
def Op(request):
    form=forms.OnlineForm()
    if request.method=='POST':
        form=forms.OnlineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Success/")
        else:
            return HttpResponseRedirect("/Failure")
    return render(request,'MyApp/Op.html',{'form':form})
def Failure(request):
    return render(request,'MyApp/Failure.html') 
'''
def LoginView(request):
    form=AuthenticationForm()
    returne render(request,'registration/login',{'form':form})
'''
def DownloadAllDetails(request):
    res = HttpResponse(content_type="text/css")
    res['content-Disposition'] = 'attachment; filename="Appointmentslist.csv"'
    write = csv.writer(res)
    qs = OnlineOp.objects.all()
    for x in qs:
        write.writerow([x.id, x.Patient_Name, x.Mobile, x.Age, x.Gender,x.Timmings])
    return res