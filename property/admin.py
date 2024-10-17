from django.contrib import admin
from .models import Flat, Complain, Owner

class OwnerInline(admin.TabularInline):
    model = Owner.owned_apartments.through
    raw_id_fields = ['owner']
    extra = 1

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = (
        'address', 
        'price', 
        'new_building', 
        'construction_year',
        'town',
        'owners_phonenumber',
        'owner_pure_phone'
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]

class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owned_apartments',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
