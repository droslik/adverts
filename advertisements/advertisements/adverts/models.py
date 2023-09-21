from django.core.validators import MinValueValidator
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.pk} - {self.name}'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class City(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Advert(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='adverts',
    )
    city = models.ForeignKey(
        City,
        default=None,
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='adverts'
    )
    views = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f'{self.pk} - {self.title}'
