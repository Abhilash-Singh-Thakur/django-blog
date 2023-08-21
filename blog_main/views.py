from django.shortcuts import render

from blogs.models import Blog, Category


def home(request):
    # step 9 : - to show all the category data into the display.
    categories = Category.objects.all()
    print(categories)

    # step 10 : - query to filter the record as per the condition.
    featured_posts = Blog.objects.filter(is_featured=True,status='Published')
    print(featured_posts)
    posts = Blog.objects.filter(is_featured=False,status='Published')
    print(posts)
    context = {
        'categories': categories,
        'featured_posts':featured_posts,
        'posts': posts,
    }
    return render(request,'home.html',context)