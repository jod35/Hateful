from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)

class PostAmin(admin.ModelAdmin):
    list_display=('name','message','title','date_created')
    search_fields=('name',)

    list_filter=('date_created','name')
