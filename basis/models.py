from django.db import models
from django.conf import settings
from enum import Enum

# Create your models here.
class CountryTag(Enum):
    """
    Enum Country Tag Model
    """
    DE = "German"
    FR = "French"
    JP = "Japanese"
    TH = "Thai"
    CA = "Canada"
    CN = "Chinese"
    CH = "Swiss"
    IN = "Indonesian"
    ES = "Spanish"
    US = "USA"
    UK = "British"
    PH = "Phillipines"

class Country(models.Model):
    """
    Country Model
    """
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Country string
        """
        return "Country : {}".format(self.name)

class Zone(models.Model):
    """
    Zone Model
    """
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=5,
        choices=[(tag, tag.value) for tag in CountryTag]
        , default='null')

    def __str__(self):
        """
        Zone string
        """
        return "Zone : {}, from {} id".format(self.name, self.country)

class PointOfInterest(models.Model):
    """
    PointOfInterest Model
    """
    title = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    address = models.CharField(max_length=200, null=False)
    link = models.URLField(blank=True, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """
        Point of Interest string
        """
        return "POI : {}".format(self.title)

class Category(models.Model):
    """
    Category Model
    """
    title = models.CharField(max_length=100, unique=True)
    point_of_interest = models.ManyToManyField(PointOfInterest)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Category string
        """
        return "Category : {}".format(self.title)

class Comment(models.Model):
    """
    Comment
    """
    content = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        """
        Comment string
        """
        return "Comment : {}, {}".format(self.content, self.user)
