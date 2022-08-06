from django.shortcuts import render, HttpResponse
from pj3.models import Register
from django.contrib import messages

# Create your views here.

def index(request):
     return render(request, 'index.html')
    #return HttpResponse("This is homepage")

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        linkedin = request.POST.get('linkedin')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')
        register = Register(name=name, email=email, linkedin=linkedin, twitter=twitter, instagram=instagram)
        register.save()
        messages.success(request, 'Submitted Successfully!')
    return render(request, 'register.html')

def employees(request):
    employee_list = Register.objects.all().order_by('name')
    return render(request, 'employees.html', 
    {'employee_list':employee_list})


