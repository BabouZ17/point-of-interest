from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Country, Category, PointOfInterest
from .forms import ContactForm, CountryForm, CategoryForm, PointOfInterestForm, ZoneForm

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
    if request.method == "GET":
        countries = Country.objects.all()
        context = {
            "countries": countries
        }
        return render(request, 'basis/board.html', context)
    elif request.method == "POST":
        return render(request, 'basis/board.html')

def pois(request):
    """
    Return the pointofinterests
    """
    pointofinterests = PointOfInterest.objects.all()
    context = {
        "pointofinterests": pointofinterests
    }
    return render(request, 'basis/pointofinterests.html', context)

def category(request, id=0):
    """
    Return the category according to the id
    """
    category = get_object_or_404(Category, pk=id)
    context = {
        "category": category
    }
    return render(request, 'basis/category.html', context)

def edit_category(request, id=0):
    """
    Edit the category with the id
    """
    is_new = False
    try:
        category = Category.objects.get(pk=id)
    except ObjectDoesNotExist:
        is_new = True
    if request.method == "GET" and is_new:
        form = CategoryForm()
        context = {
            "form": CategoryForm()
        }
        return render(request, 'basis/edit_category.html', context)
    elif request.method == "GET" and not is_new:
        form = CategoryForm(instance=category)
        context = {
            "form": form,
            "category": category
        }
        return render(request, 'basis/edit_category.html', context)
    elif request.method == "POST" and is_new:
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category added!")
        else:
            messages.error(request, "Category not added!")
        return render(request, 'basis/categories.html')
    elif request.method == "POST" and not is_new:
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category.name = category_form.cleaned_data.get('title')
            category.updated_at = timezone.now()
            category.tag = category_form.cleaned_data.get('tag')
            category.country = Country.objects.get(category_form.cleaned_data.get('country'))
            category.save()
            messages.success(request, "Country edited!")
        else:
            messages.error(request, "Country not edited!")
        return render(request, 'basis/countries.html')
    else:
        messages.error(request, "Unknown request")
        return HttpResponseRedirect(reverse('basis:home'))

def categories(request):
    """
    Return the categories
    """
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'basis/categories.html', context)

def country(request, id=0):
    """
    Return the country according to the id
    """
    country = get_object_or_404(Country, pk=id)
    context = {
        "country": country
    }
    return render(request, 'basis/country.html', context)

def edit_country(request, id=0):
    """
    Edit the country with the id
    """
    is_new = False
    try:
        country = Country.objects.get(pk=id)
    except ObjectDoesNotExist:
        is_new = True
    if request.method == "GET" and is_new:
        form = CountryForm()
        context = {
            "form": CountryForm()
        }
        return render(request, 'basis/edit_country.html', context)
    elif request.method == "GET" and not is_new:
        form = CountryForm(instance=country)
        context = {
            "form": form,
            "country": country
        }
        return render(request, 'basis/edit_country.html', context)
    elif request.method == "POST" and is_new:
        country_form = CountryForm(request.POST)
        if country_form.is_valid():
            country_form.save()
            messages.success(request, "Country added!")
        else:
            messages.error(request, "Country not added!")
        return render(request, 'basis/countries.html')
    elif request.method == "POST" and not is_new:
        country_form = CountryForm(request.POST)
        if country_form.is_valid():
            country.name = country_form.cleaned_data.get('name')
            country.save()
            messages.success(request, "Country edited!")
        else:
            messages.error(request, "Country not edited!")
        return render(request, 'basis/countries.html')
    else:
        messages.error(request, "Unknown request")
        return HttpResponseRedirect(reverse('basis:home'))

def countries(request):
    """
    Return the countries
    """
    countries = Country.objects.all()
    context = {
        "countries": countries
    }
    return render(request, 'basis/countries.html', context)

def pointofinterests(request):
    """
    Return the pois
    """
    pois = PointOfInterest.objects.all()
    context = {
        "pois": pois
    }
    return render(request, 'basis/pointofinterests.html', context)
