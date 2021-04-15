'''
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    text={
        'name':'Md.Sohel Rana',
        'age':24,
        'phone':'01776363070',
        'friend_name': ['Polash', 'Fahim', 'Rifat', 'Opu', 'Sumon']
    }

    return render(request,'index.html',text)


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
'''