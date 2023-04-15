from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm
from service.models import Service
from contactenquiry.models import contacteEnquiry
from news.models import news
from django.core. paginator import Paginator

def homepage(request):
    newsdata=news.objects.all()
    servicesData=Service.objects.all().order_by('id')#[:2]
    data={
        'servicesData': servicesData,
        'newsdata':newsdata
    }

    return render(request,"index.html",data)

def newsdetail(request,slug):
    print(slug)
    newsdetail=news.objects.get(news_slug=slug)
    data={
        'newsdetail':newsdetail
    }
    return render(request,"newsdetail.html  ",data)

def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"about.html",{'output':output})

def hosting(request):
    serviceData=Service.objects.all()
    paginator=Paginator(serviceData,1)
    page_number=request.GET.get('page')
    serviceDatafinal=paginator.get_page(page_number)
    totalpage=serviceDatafinal.paginator.num_pages
    #if request.method=="GET":
    #    st=request.GET.get('servicename')
    #   if st!=None:
    #       servicesData=Service.objects.filter(service_title__icontains=st)

    data={
        'servicesData': serviceDatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n  in range(totalpage)]
    }
    
    return render(request,"hosting.html",data)


def submitform(request):
    try:
        n1=int (request.POST.get('num1'))
        n2=int (request.POST.get('num2'))
        finalans=n1+n2
        data={
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
        return HttpResponse(finalans)
    except:
        pass

def domain(request):
    return render(request,"domain.html")

def contact(request):
    return render(request,"contact.html")

def saveEnquiry(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Phone=request.POST.get('Phone')
        Message=request.POST.get('Message')
        en=contacteEnquiry(name=Name,email=Email,phone=Phone,message=Message)
        en.save()
    return render(request,"contact.html")
    
def form(request):
    finalans=0
    fn=usersForm()
    data= {'form':fn}
    try:
        n1=int (request.POST.get('num1'))
        n2=int (request.POST.get('num2'))
        finalans=n1+n2
        data={
            'form':fn,
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
        url="/about/?output={}".format(finalans)
        return redirect(url)
    except:
        pass
    return render(request,"form.html",data)

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr =="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr =="/":
                c=n1/n2
    except:
        c="invalid opr"
    print(c)
    return render(request, "calculator.html", {'c':c})

def saveevenodd (request):
    c=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error':True})

        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="even number"
        else:
            c="ood number"
    return render(request, "evenodd.html", {'c':c})

def marksheet (request):
    if request.method=="POST":
        s1=eval(request.POST.get('Subject1'))
        s2=eval(request.POST.get('Subject2'))
        s3=eval(request.POST.get('Subject3'))
        s4=eval(request.POST.get('Subject4'))
        s5=eval(request.POST.get('Subject5'))
        t=s1+s2+s3+s4+s5
        
        p=t*100/500; 
        if p>=80:
            d="first class"
        elif p>=70:
            d="second class"
        elif p>=60:
            d="third class"
        elif  p<=33:
            d="u r fail"
            
        data={
            'total':t,
            'per':p,
            'div':d,
        }
        return render(request, "marksheet.html",data)

    return render(request, "marksheet.html")
