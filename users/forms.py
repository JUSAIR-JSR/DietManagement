from django import forms
from django.contrib.auth.models import User
from .models import Customer

class CustomerProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Add email field from the User model

    class Meta:
        model = Customer
        fields = ['profile_photo', 'phone_number', 'address', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill the email field with the current user's email
        if self.instance.user:
            self.fields['email'].initial = self.instance.user.email

        # Add Tailwind CSS classes to each form field
        self.fields['profile_photo'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded-lg mb-4'
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded-lg mb-4',
            'placeholder': 'Enter your phone number'
        })
        self.fields['address'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded-lg mb-4',
            'placeholder': 'Enter your address'
        })
        self.fields['location'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded-lg mb-4',
            'placeholder': 'Enter your location'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded-lg mb-4',
            'placeholder': 'Enter your email'
        })

    def save(self, commit=True):
        # Save the Customer profile
        customer = super().save(commit=False)
        if commit:
            customer.save()
            # Update the associated User's email
            user = customer.user
            user.email = self.cleaned_data['email']
            user.save()
        return customer