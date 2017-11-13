from django.contrib import admin

from .models import Author
from .models import Book
from .models import Forum
from .models import Comentary
# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Forum)
admin.site.register(Comentary)
