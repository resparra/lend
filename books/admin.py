from django.contrib import admin
from books.models import Book, User

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['title']}),
        ('Author',		 	{'fields': ['author']}),
        ('Publication', 	{'fields': ['pub_year']}),
        ('Edition', 	 	{'fields': ['edition']}),
        ('Lend to', 	 	{'fields': ['user']}),
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(User)
