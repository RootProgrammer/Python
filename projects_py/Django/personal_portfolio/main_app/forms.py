from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name Here. Please enter at least 4 chars'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a valid email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter at least 8 chars of subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please write something for Me'}),
        }
