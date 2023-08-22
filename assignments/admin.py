from django.contrib import admin
from django.http.request import HttpRequest
from . models import About, SocialLink
# Register your models here.


# Logic to disable the add button in the admin panel if you have one data in about model
# this is the class to change the model admin and overwrite the method as poer condintion.
class AboutAdmin(admin.ModelAdmin):
    # this method will give the permission to add any data in our admin panel

    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False

# Register the model into admin site.
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)