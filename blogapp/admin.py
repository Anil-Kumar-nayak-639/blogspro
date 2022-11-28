from django.contrib import admin
from blogapp.models import category,post
# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ('title','description','url',)
    search_fields = ('title',)

admin.site.register(category,categoryadmin)

class postadmin(admin.ModelAdmin):
    list_display = ('title','content','url','image',)
    search_fields = ('title',)


admin.site.register(post,postadmin)