from django.db import models
#from django.urls import reverse
#from django.contrib import admin

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [        
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True
        )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

"""
class Photo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='product_images/')
    thumbnail_image = models.ImageField(upload_to='product_images/', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.thumbnail_image and not self.original_image:
            try:
                from PIL import Image
                img = Image.open(self.original_image.path)
                img.thumbnail((200, 200))
                img.save(self.thumbnail_image.path)
            except Exception as e:
                print(f"Error creating thumbnail: {e}")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('my_app:my_model_detail', args=[self.pk])
    
class PhotoInline(admin.TabularInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
"""