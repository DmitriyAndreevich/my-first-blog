from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('your_name', 'your_email', 'your_phone', 'your_message')