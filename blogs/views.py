from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from . models import Blog, Category, Comment
from django.db.models import Q
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


# take the single blog which matches the slug.
def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,

    }
    return render(request, 'blogs.html', context)




def search(request):
    keyword = request.GET.get('keyword')         # , is consider as end operator
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,

    }
    return render(request, 'search.html', context)