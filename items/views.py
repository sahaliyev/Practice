from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import UploadPicture
from django import forms
from .forms import UserForm, ProductForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
import smtplib
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


def index(request):
    data = {}
    data['title'] = UploadPicture.objects.all()
    title = UploadPicture.objects.filter().order_by('-time')
    paginator = Paginator(title, 6)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    data['title'] = posts
    return render(request, 'index.html', data)



def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        content = "%s %s %s %s" % (name, subject, message, email)
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('sahil.eyev@gmail.com', 'Sahil751')
        mail.sendmail('sahil.aliyev.751@gmail.com', 'sahil.eyev@gmail.com', content)
        mail.close()
        return HttpResponseRedirect('/contact')
    else:
        pass
    return render(request, 'contact.html')

def man(request):
    data = {}
    data['title'] = UploadPicture.objects.all()
    title = UploadPicture.objects.filter(choose=1).order_by('-time')
    paginator = Paginator(title, 6)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    data['title'] = posts
    return render(request, 'man.html', data)

def woman(request):
    data = {}
    data['title'] = UploadPicture.objects.all()
    title = UploadPicture.objects.filter(choose=2).order_by('-time')
    paginator = Paginator(title, 6)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    data['title'] = posts
    return render(request, 'woman.html', data)

def children(request):
    data = {}
    data['title'] = UploadPicture.objects.all()
    title = UploadPicture.objects.filter(choose=3).order_by('-time')
    paginator = Paginator(title, 6)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    data['title'] = posts
    return render(request, 'children.html', data)

def post(request, title):
    try:
        data = {}
        data['price'] = UploadPicture.objects.get(title = title)
    except UploadPicture.DoesNotExist:
        return redirect('/')
    return render(request, 'post.html', data)

def log(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
            request, "You successfully logged in!"
            )
            return redirect('/')
        else:
            messages.error(
            request, "Username and password does not match! Please, try again."
            "If you do not have account go and register by clicking 'Join us'"
            )
            return redirect('/login')
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'log.html')

def register(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            messages.success(
            request, "You successfully registered!"
            )
            return redirect('/')
        else:
            messages.error(
            request, "Your email address is not correct. Please, try again"
            )
            return redirect('/register/')
    else:
        pass
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'register.html')

def upload(request):
    context = {}
    context['form'] = ProductForm()
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    #     else:
    #         return redirect('/')
    # else:
    #     context['form'] = ProductForm()

    if request.user.is_authenticated:
        return render(request, 'upload.html', context)
    else:
        return redirect('/')
