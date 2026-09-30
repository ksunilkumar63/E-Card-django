# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ECard


@admin.register(ECard)
class ECardAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'price',
        'created_at'
    )

    search_fields = (
        'title',
        'category'
    )

    list_filter = (
        'category',
    )
