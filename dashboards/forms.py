# for add the category form 

from django import forms

from blogs.models import Blog, Category



class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


# creted the model form by loading the Blog Field.
class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title','category', 'featured_image','short_description', 'blog_body', 'status', 'is_featured')


        