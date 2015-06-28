from django.contrib import admin
from blog.models import posts
from  blog.models import AboutMe
# Register your models here.


admin.site.register(posts)

admin.site.register(AboutMe)