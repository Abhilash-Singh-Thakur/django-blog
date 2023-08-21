from django.shortcuts import redirect, render

from . models import Blog, Category

# Create your views here.

# this is if we will click on the link and open the page.
def posts_by_category(request, category_id):
    # Fetch the posts that belong to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # whenever you will use the get method then you need to use the try catch method. to handle the error.
    try:
        category = Category.objects.get(pk=category_id)
    except:
       # if user is not found then it will return the user to home page.
       return redirect('home')
    #    or when the category does not exist then get the 404 page.
    # category = get_object_or_404(Category, pk=category_id)

    context = {
            'posts': posts,
            'category': category,
    }
    return render(request, 'posts_by_category.html', context)


