from django.shortcuts import render,redirect
from . import forms
from .models import Employee_Model
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'crudapp/index.html')


def add_employee(request):
    if request.method == "POST":
        form = forms.Emp_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee created Successfully !")        
            return redirect('/add_employee')
        else:
            emp_form = forms.Emp_Form()
            context={
                'form':emp_form,
                }
            return render(request, 'crudapp/add_employee.html' , context)
    else:
        emp_form = forms.Emp_Form()
        context={
            'form':emp_form,
        }
        return render(request, 'crudapp/add_employee.html' , context)
    
def read(request):
    data = Employee_Model.objects.all()
    context = {
        'data':data
    }
    return render(request,'crudapp/list.html', context)


def update(request, id):
    emp = Employee_Model.objects.get(id=id)
    if request.method =="POST":
        form = forms.Emp_Form(request.POST, instance=emp)
        if form.is_valid():
            form.save()
        return redirect('/list')
    else:
        context = {'data':emp}
        return render(request,'crudapp/update.html',context)

def delete(request, id):
    emp  = Emp_Model.objects.get(id=id)
    emp.delete()
    return redirect('/list')



#authentication ----------------------------------------------------
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm


# Create your views here.
# Home page
def index(request):
    return render(request, 'crudapp/home.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'crudapp/register.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                #return render(request, 'crud_app/index.html')
                return redirect('/index')
    else:
        form = LoginForm()
    return render(request, 'crudapp/login.html', {'form': form})


"""
# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
"""
