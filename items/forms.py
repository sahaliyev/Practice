from django import forms
from django.contrib.auth.models import User
from .models import UploadPicture

class ProductForm(forms.Form):
    title = forms.CharField(max_length=200)
    price = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    madein = forms.CharField(max_length=200)
    image = forms.FileField()
    # class Meta:
    #     model=UploadPicture
    #     fields = ['title', 'price', 'description', 'madein', 'image']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','last_name', 'email', 'password']
