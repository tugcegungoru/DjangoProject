from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from car.models import Car, Category
from home.models import Setting, ContactFormu, ContactFormMessage

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Car.objects.all()[:4]
    category = Category.objects.all()
    daycars= Car.objects.all()[:5]
    #lastcars = Car.objects.all().order_by('-id')[:4]
    #randomcars = Car.objects.all().order_by('?')[:4]

    context= {'setting': setting,
              'category': category,
              'page':'home',
              'sliderdata':sliderdata,
              'daycars': daycars}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context= {'setting': setting,
              'category': category}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context= {'setting': setting,
              'category': category,
              }
    return render(request, 'referanslar.html', context)

def iletisim(request):      #formu kaydetmek için
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarı ile gönderilmiştir.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)   #forma ulaşmak için
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting,
               'form':form,
               'category': category}
    return render(request, 'iletisim.html', context)


def category_cars(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    cars = Car.objects.filter(category_id=id)
    context= {'cars': cars,
              'category': category,
              'categorydata':categorydata}
    return render(request, 'cars.html', context)