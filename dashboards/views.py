from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm

# dynamic count of post and blogs are showing.

@login_required(login_url='login')# if the user is not loggedin then it will forcefully redirect to login url page.
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        "category_count": category_count,
        "blogs_count": blogs_count,
    }
    return render(request, "dashboard/dashboard.html", context)




def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form =CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)



def edit_category(request, pk):
    # load the model form for the category
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return  redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html',context)



def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')