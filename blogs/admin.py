from django.contrib import admin

from blogs.models import Blog, Category

# based on the title slug should be generated.

# step 4
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug' : ('title',)}
    # step 6 - list all the fields in the admin panel
    list_display = ('title', 'category', 'author','featured_image','short_description','status', 'is_featured', 'updated_at')
    # step 7 - create the search field and search by this category.
    search_fields = ('id', 'title', 'category__category_name','status')
    #step 8
    #list_editable= ( 'category', 'author','featured_image','short_description','status', 'is_featured')
    list_editable= ('is_featured',)


# Register your models here.
admin.site.register(Category)

# step 5 add the BlogAdmin
admin.site.register(Blog, BlogAdmin) # then register the blogAdmin in admin site.