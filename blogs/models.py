from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # to correct the spelling of categories changing the metadata.
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ('Draft','Draft'),
    ('Published','Published')
)

# step 2
class Blog(models.Model):
    title =  models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # means when we delete the category then the blog post of that category also will deleted. 
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user delete then all blog also get deleted.
    featured_image = models.ImageField(upload_to='upload/%y/%m/%d', height_field=None, width_field=None, max_length=None)
    short_description = RichTextField()
    blog_body = RichTextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # step 3
    def __str_(self):
        return self.title

# run the command make migration and migrate.


