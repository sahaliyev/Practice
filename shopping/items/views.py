from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import UploadPicture
from .forms import Form
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import smtplib


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
        form = Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            content = "%s %s %s %s" % (name, subject, message, email)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('sahil.eyev@gmail.com', 'Sahil751')
            mail.sendmail('sahil.aliyev.751@gmail.com', 'sahil.eyev@gmail.com', content)
            mail.close()
            return HttpResponseRedirect('/contact')
        else:
            return HttpResponseRedirect('/contact')
    else:
        form = Form()
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
