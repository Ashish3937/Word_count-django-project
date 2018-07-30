from django import forms

class ContactForm(forms.Form):
    
    number=forms.CharField()
