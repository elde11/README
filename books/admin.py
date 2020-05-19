from django.contrib import admin
from .models import Author, Book, Category

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = ('birth_date')
    list_display = ('first_name','last_name','birth_date','web_site')
    list_filter = ('first_name','last_name','birth_date','web_site')
    search_fields = ('last_name','first_name','author__firts_name','author__last_name')
    #Book.objects.filter(author__first_name__startswith='Andrzej')

class BookAdmin(admin.ModelAdmin):
    list_display =('title','author'
    , 'pages','description')
    list_filter = ('title','description','pages','author')
    search_fields = ('title','description')
    autocomplete_fields = ['author']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter = ('name',)
    search_fields = ('name','description')
    
   
# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
