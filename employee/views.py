from django.shortcuts import render
from django.http import HttpResponse

def employee(request):
    return HttpResponse("This is our employee module home page")
def profile(request):
    return render(request,'employee/profile.html')
def contact(request):
    return HttpResponse("This is our contact page")



