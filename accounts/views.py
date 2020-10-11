from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.
def register(request):
    if(request.method == 'POST'):
        first_nm    = request.POST['f_name']
        last_nm     = request.POST['l_name']
        user_nm     = request.POST['u_name']
        user_email  = request.POST['u_email']
        user_pass1  = request.POST['pwd1']
        user_pass2  = request.POST['pwd2']
        if(user_pass1 == user_pass2):
            if(User.objects.filter(username = user_nm).exists()):
                messages.info(request,'Username already taken. Please try another')
            elif(User.objects.filter(email = user_email).exists()):
                messages.info(request,'Email already exists!!!')
            else:
                user_obj = User.objects.create_user(first_name = first_nm,
                                                    last_name = last_nm,
                                                    username = user_nm,
                                                    email = user_email,
                                                    password = user_pass1)
                user_obj.save()
               # messages.info(request,'User Created!!')
                return redirect('loginpage')
        else:
            #print("Passwords do not match. Please retype")
            messages.info(request,'Passwords do not match. Please retype')
        return redirect('registerpage')   
    else:
        return render(request,'register.html')


def login(request):
    if(request.method == 'POST'):
        l_user_nm = request.POST['l_u_name']
        l_password = request.POST['l_pwd']

        user_lobj = auth.authenticate(username = l_user_nm, password = l_password)

        if user_lobj is not None:
            auth.login(request,user_lobj)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('loginpage')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')