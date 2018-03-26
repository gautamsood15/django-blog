from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.contrib import auth      # user auth system creates tables in the db to store username and password
#from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect   # cross site request forgery(security measure)
from forms import MyRegistrationForm



def login(request):
    c = {}
   # older version= c.update(csrf(request))
    return render(request,'login.html',c)

def auth_views(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid_login')
    

def loggedin(request):  
    return render_to_response('loggedin.html',{'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')





def register_user(request):
    
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_vaild():
            form.save();
            return HttpResponseRedirect('/accounts/register_success')
        else:
            return HttpResponseRedirect('/accounts/register_failed')
    else:
        form = MyRegistrationForm()
        return render(request,'register.html',{'form':form})

def register_success(request):
    return render_to_response('register_success.html')


        