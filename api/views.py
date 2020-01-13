from django.shortcuts import render
from .models import Api

# Create your views here.


def Storedata(request):
    fn = request.POST['fn']
    mn = request.POST['mn']
    ln = request.POST['ln']
    age = request.POST['age']
    gender = request.POST['gen']
    ph = request.POST['ph']
    ql = request.POST['ql']
    rov = request.POST['rov']

    user = Api.objects.create(Fname=fn,Mname=mn,Lname=ln,age=age,Gender=gender,phone_no=ph,Qualification=ql,R_o_v=rov)
    user.save()
    return render(request,'index.html')