from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        query = f"SELECT * FROM student_student WHERE username = '{username}' AND password = '{password}'" 
        stud =  Student.objects.raw(query)
        if len(stud) > 0:
            u = stud[0]
            user = authenticate(username=u.username, password=u.password)
            print(user)
            if user is not None:
                print("LOG in user")
                login(request, user)
                return redirect('/flag')
            else:
                return render(request,'index.html',{'error':'invalid credentials'})
        else:
            return render(request,'index.html',{'error':'invalid credentials'})

    return render(request,'index.html')

@login_required
def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
