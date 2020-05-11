from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from home.forms import SearchForm, SignUpForm
# Create your views here.
from car.models import Car, Category, Images, Comment
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

def car_detail(request,id,slug):
    category = Category.objects.all()
    car = Car.objects.get(pk=id)
    images = Images.objects.filter(car_id=id)
    randomcars = Car.objects.all().order_by('?')[:4]
    comments = Comment.objects.filter(car_id=id,status='True')
    context = {'car': car,
               'category': category,
               'images': images,
               'randomcars': randomcars,
               'comments': comments}
    return render(request, 'car_detail.html' , context)

def car_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            cars = Car.objects.filter(title__icontains=query)
            context = {'cars': cars,
                       'category': category}
            return render(request, 'cars_search.html',context)
    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Kullanıcı adı veya şifre hatalı!")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form}
    return render(request, 'signup.html', context)