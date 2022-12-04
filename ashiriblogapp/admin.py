from django.contrib import admin
from .models import blogs
# Register your models here.



#admin.site.register(blogs)
@admin.register(blogs)
class blogsAdmin(admin.ModelAdmin):
		list_display = ('title', 'published', 'author')
		date_hierarchy = 'published'
		search_fields = ('title', 'location')