from django import forms

class Form(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    subject = forms.CharField(label='Subject', max_length=20)
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length=2000)
