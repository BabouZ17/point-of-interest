from django import forms
from django.forms import ModelForm
from .models import Country, Zone, PointOfInterest, Comment, Category

class ContactForm(forms.Form):
    first_name = forms.CharField(
        label='First name :',
        initial='james...',
        help_text='Please fill with your first name.',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )
    last_name = forms.CharField(
        label='Last name :',
        initial='rodgers...',
        help_text='Please fill with your last name.',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )
    email = forms.EmailField(
        label='Email :',
        initial='james.rodgers@gmail.com',
        help_text='Please fill with your email.',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
        )
    message = forms.CharField(
        label='Message :',
        initial='Hi there...',
        widget=forms.Textarea,
        max_length=500,
        required=True
        )

class CountryForm(ModelForm):
    """
    Country Form
    """
    class Meta:
        model = Country
        fields = ['name']

class ZoneForm(ModelForm):
    """
    Zone Form
    """
    class Meta:
        model = Zone
        fields = ['name', 'country', 'tag']

class PointOfInterestForm(ModelForm):
    """
    PointOfInterest Form
    """
    class Meta:
        model = PointOfInterest
        fields = ['title', 'description', 'latitude', 'longitude', 'address', 'link', 'zone', 'author']

class CategoryForm(ModelForm):
    """
    Category Form
    """
    class Meta:
        model = Category
        fields = ['title', 'point_of_interest']
