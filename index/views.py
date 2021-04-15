from django.shortcuts import render
from .models import aboutus
from .models import slider
from .models import clientinfo
from .models import portfolio


# Create your views here.
def home(request):
    aboutusdata=aboutus.objects.all()[0]
    sliderdata = slider.objects.all()
    clientinfodata = clientinfo.objects.all()
    portfoliodata = portfolio.objects.all()


    context={
        'aboutus':aboutusdata,
        'slider': sliderdata,
        'clientinfo': clientinfodata,
        ' portfolio': portfoliodata


    }

    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')




