from . models import Category


# This is the context processors function to get the dictionaty of categories.
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)
