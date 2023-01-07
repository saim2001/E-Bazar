from django.shortcuts import render
from django.http import HttpResponse,request,Http404,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
def index(request):
    return render(request,'User_registration.html')

def signin(request):
    pass
@csrf_exempt
def register(request):

    user_mdl=User(user_Name=request.POST.get('user_name'),user_Password = request.POST.get('password'),user_email_phone = request.POST.get('Mob_or_Eml'))

    user_mdl.save()
    print(request.POST.get('username'))
    return HttpResponse(request.POST.get('user_name'))
        #     HttpResponse(request,"password do not match")



