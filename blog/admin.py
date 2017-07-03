from django.contrib import admin
from .models import Post

# To make model visible on admin page, need to register model with: 
admin.site.register(Post)
