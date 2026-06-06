from django.contrib import admin
from blog.models import Post , category
class PostAdmin(admin.ModelAdmin):
        date_hierarchy = 'created_date'
        empty_value_display = '---'
        list_display = ('title','author','counted_views','published_date', 'status', 'created_date', 'updated_date','image')
        list_filter = ('status','author')
        search_fields = ['title','content']

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(category)