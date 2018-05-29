from django import forms

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
