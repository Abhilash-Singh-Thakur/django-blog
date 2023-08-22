from assignments.models import SocialLink
from . models import Category


# This is the context processors function to get the dictionaty of categories.
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


# This is the context processors function to get the dictionaty of social links that we can use any where.
def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)
