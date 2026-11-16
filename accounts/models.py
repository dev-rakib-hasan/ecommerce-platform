from django.db import models
from django.utils.text import slugify

# Create your models here.

def generate_unique_slug(instance, value):
    base_slug = slugify(value)
    
    if not base_slug:
        base_slug = instance._meta.model_name
    slug = base_slug
    counter = 1
    
    queryset = instance.__class__.objects.all()
    
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)
        
    while queryset.filter(slug=slug).exists():
        slug = f'{base_slug}-{counter}'
        counter+=1
        
    return slug
    
    
class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwargs)
            
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories',
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwagrs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save(*args, **kwagrs)    

    def __str__(self):
        return self.name
    
class Product(models.Model):
    STATUS_CHOICES = [
        ('draft','Draft'),
        ('published', "Published"),
        ('archivrd', 'Archived'),
    ]
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    sku = models.CharField(max_length=150, unique=True)
    brand = models.ForeignKey(
        Brand,
        on_delete= models.SET_NULL,
        null= True,
        blank= True,
        related_name= 'products',
    )
    category= models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        max_digits= 10,
        decimal_places= 2,
        null= True,
        blank= True,
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    stock = models.PositiveBigIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.BooleanField(default=True)
    updated_at = models.BooleanField(default=True)