from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    model = Book

# Define the admin class
# class AuthorAdmin(admin.ModelAdmin):
#     list_filter = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     inlines = [BooksInstanceInLine]
    
#     fieldsets = (
#             (None, {
#                 'fields': ('book', 'imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back')
#         }))
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#    inlines = [BooksInline]

# Register the admin class with the associated model
#admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator

#@admin.register(BookInstance)
#class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance  

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
#    inlines = [BooksInstanceInline]

admin.site.register(Book, BookAdmin)

# Register the Admin classes for BookInstance using the decorator
#admin.site.register(Book, BookAdmin) 

admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

#@admin.site.register(Book, BookAdmin)
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
  