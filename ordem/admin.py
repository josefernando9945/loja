from django.contrib import admin
from django.contrib import admin

from ordem.models import Cliente, Item, Ordem



class ClienteAdminTbularInline(admin.TabularInline):
    model = Cliente


class ItemAdminTabularInline(admin.TabularInline):
    model = Item


class OrdemAdmin(admin.ModelAdmin):
    model = Ordem
    inlines = [ItemAdminTabularInline]


admin.site.register(Cliente)
admin.site.register(Ordem, OrdemAdmin)

