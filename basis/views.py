from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

from .models import Country, Category
from .forms import ContactForm

# Create your views here.
def home(request):
    """
    Home page
    """
    context = {
        "content": "Welcome Guys !"
    }
    return render(request, 'basis/home.html', context)

def contact(request):
    """
    Contact form management
    """
    if request.method == "GET":
        context = {
            "form": ContactForm()
        }
        return render(request, 'basis/contact.html', context)
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            success = send_mail(
                'Message from: ' + form.cleaned_data['first_name'] + ' ' +
                form.cleaned_data['last_name'] + ' ' +
                form.cleaned_data['email'],
                form.cleaned_data['message'],
                'no-reply@com',
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            if success:
                messages.success(request, 'Mail Sent To The Admin !')
            else:
                messages.error(request, 'Failed to deliver the mail !')
    else:
        messages.error(request, 'Error in your request ')
    return HttpResponseRedirect(reverse('basis:contact'))

def board(request):
    """
    Return the board view
    """
    return render(request, 'basis/board.html')

def categories(request):
    """
    Return the categories
    """
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'basis/categories.html', context)
    
def countries(request):
    """
    Return the countries
    """
    countries = Country.objects.all()
    context = {
        "countries": countries
    }
    return render(request, 'basis/countries.html', context)
