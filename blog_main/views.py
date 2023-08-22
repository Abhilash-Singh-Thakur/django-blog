from django.shortcuts import render
from assignments.models import About

from blogs.models import Blog, Category


def home(request):
    # step 9 : - to show all the category data into the display.
    # categories = Category.objects.all()
    # step 10 : - query to filter the record as per the condition.
    featured_posts = Blog.objects.filter(is_featured=True,status='Published')
    posts = Blog.objects.filter(is_featured=False,status='Published')
    

    # with get method always use the try block.
    
    try:
        about = About.objects.get()
    except:
        about = None
    
    context = {
        # 'categories': categories,
        'featured_posts':featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request,'home.html',context)