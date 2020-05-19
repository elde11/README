from django.contrib import admin

from django.contrib import admin
from .models import Review, Grade, ReviewManager

class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = ('pub_date')
    list_display = ('title','book','content','pub_date','grade','STATE_CHOICES','state')
    list_filter = ('user','title','book','pub_date','grade','state')
    search_fields = ('pub_date','title','book','state','grade','state')
    #Book.objects.filter(author__first_name__startswith='Andrzej')

class GradeAdmin(admin.ModelAdmin):
    list_display =('grade','book'
    , 'user')
    list_filter = ('book','grade','user')
    search_fields = ('book','grade')
    autocomplete_fields = ['book']


   
# Register your models here.
admin.site.register(Review, ReviewAdmin)
admin.site.register(Grade, GradeAdmin)
