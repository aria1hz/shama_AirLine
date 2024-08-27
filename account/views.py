from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import RegisterForm,LoginForm
from .models import User
from django.contrib.auth import login,logout
from django.utils.crypto import get_random_string

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = request.POST.get('email')
            user_pass = request.POST.get('password')
            user = User.objects.get(email__iexact=user_email)
            check_password = user.check_password(user_pass)
            if check_password:
                login(request,user)
                return redirect(reverse('home:home'))
            else:
                print('error')
        
    return render(request, 'account/login.html',{'form':LoginForm})





def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_email= request.POST.get('email')
            user =User.objects.filter(email__iexact=user_email).exists()
            if user:
                form.add_error('email','این ایمیل قبلا ثبت شده است')
                return render(request,"account/signup.html", {'form' : form} )
            else:
                user_pass= request.POST.get('password')
                user_user=request.POST.get('user_name')
                new_user= User(email=user_email,username=user_user, is_active=False)
                new_user.set_password(user_pass)
                new_user.email_active_code=get_random_string(100)
                new_user.save()
                return redirect(reverse('account:login'))
            #bara in ye page besaz Ke bege email khod ra check namayid
        else:
            return render(request,"account/signup.html", {'form' : form} )
    return render(request,"account/signup.html", {'form' : RegisterForm} )




def logout(request):
    logout(request)
    return redirect(reverse('account:login'))










# def login(request):
#     # if request.user.is_authenticated :
#     #     return redirect(reverse('home:home'))
#     if request.method=='POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             user_email=request.POST.get('email')
#             user = User.objects.filter(email__iexact=user_email)
#             if user is not None:
#                 user_pass=request.POST.get('password')
#                 passwordcheck=user.check_password(user_pass)
#                 if user.is_active == False:
#                     form.add_error('email',' ایمیل  فعال هنوز نشده است')
#                     return render(request,"account/login.html", {'form' : form})
#                 else:
#                     if passwordcheck:
#                         login(request,user)
#                     else:
#                         form.add_error('password','رمز عبور یا ایمیل  یافت نشد')
#                         form.add_error('user_name','رمز عبور یا ایمیل  یافت نشد')
#                         return render(request,"account/login.html", {'form' : form})
                    
#             else:
#                 form.add_error('password','رمز عبور یا ایمیل  یافت نشد')
#                 form.add_error('password','رمز عبور یا ایمیل  یافت نشد')
#                 return render(request,"account/login.html", {'form' : form})
#     return render(request,"account/login.html", {'form' : LoginForm})
