from django.contrib import admin
from blog.models import Post
class PostAdmin(admin.ModelAdmin):
        date_hierarchy = 'created_date'
        empty_value_display = '---'
        list_display = ('title','counted_views','published_date', 'status', 'created_date', 'updated_date')
# Register your models here.
admin.site.register(Post,PostAdmin)