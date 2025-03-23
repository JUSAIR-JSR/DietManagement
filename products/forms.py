from django import forms
from .models import Product, Category, Species

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'calories_per_100g', 'stock', 'category', 'species']

    # Customize form fields with Tailwind CSS classes
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500'
        })
    )

    species = forms.ModelMultipleChoiceField(
        queryset=Species.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'border border-gray-300 rounded-lg p-2'
        })
    )

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500',
        'rows': 3
    }))

    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500'
    }))

    image = forms.FileInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500'
    })

    calories_per_100g = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500'
    }))

    stock = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500'
    }))