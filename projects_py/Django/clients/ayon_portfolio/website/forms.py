from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'message']
		widgets = {
                    'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name Here.'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a valid email'}),
                    'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please write something for Me'}),
        }
