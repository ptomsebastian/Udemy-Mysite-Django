from django.contrib import admin
from .models import Post, Author, Tag, Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter=('author','tags','date')
    list_display=('title','date', 'author') # for how the viewing should be in admin panel
    prepopulated_fields = {'slug': ('title',)}

class CommentsAdmin(admin.ModelAdmin):
    list_display=('user_name', 'post')

admin.site.register(Post, PostAdmin) #register for viewing in admin panel
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comments, CommentsAdmin)