from django.contrib import admin
from .models import Post,Category,Comment,PostImage,Like


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostImage)
admin.site.register(Comment)
admin.site.register(Like)
