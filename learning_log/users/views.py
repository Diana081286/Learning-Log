from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from .forms import RegisterForm,EmailLoginForm
from django.contrib.auth.views import LoginView

def register_vew(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('learning_logs:index')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

class CustomLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = 'users/login.html'

def logout_view(request):
    logout(request)
    return redirect('learning_log:index')





