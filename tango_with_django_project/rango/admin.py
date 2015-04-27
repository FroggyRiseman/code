from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)


class PageAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'url']

admin.site.register(Page, PageAdmin)
