from django.contrib import admin

# Register your models here.
from .models import Blog
from .models import Comment
from .models import Log
from .models import Friend
from .models import Music
 
 
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Log)
admin.site.register(Friend)
admin.site.register(Music)