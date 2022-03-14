from django.shortcuts import render
from .models import Student
from django.contrib.auth import authenticate

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
            if user is not None:
                return render(request,'home.html',{'user':user})
            else:
                return render(request,'index.html',{'error':'invalid credentials'})
        else:
            return render(request,'index.html',{'error':'invalid credentials'})

    return render(request,'index.html')
