from django.db import models
from accounts.models import Category
from django.urls import reverse
from django.db.models.deletion import CASCADE
# Create your models here.
class Stock(models.Model):
    stock_name     = models.CharField(max_length=200, blank=True)
    slug             = models.SlugField(max_length=200, blank=True)
    description      = models.TextField(blank=True, max_length=1000)
    images           = models.ImageField(upload_to='photos/stock', blank=True)
    category         = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date     = models.DateTimeField(auto_now_add=True)
    modified_date    = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('stock_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.stock_name