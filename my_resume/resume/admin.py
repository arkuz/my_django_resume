from django.contrib import admin
from .models import Resume, MoreContacts, Works


class MoreContactsInLine(admin.TabularInline):
    model = MoreContacts

    list_display = [
        'title',
    ]
    list_display_links = [
        'title',
    ]
    search_fields = [
        'title',
    ]


class WorksInLine(admin.TabularInline):
    model = Works

    list_display = [
        'company',
        'position',
    ]
    list_display_links = [
        'company',
        'position',
    ]
    search_fields = [
        'company',
        'position',
    ]


class ResumeAdmin(admin.ModelAdmin):
    inlines = [
        MoreContactsInLine,
        WorksInLine,
    ]

    list_display = [
        'lastname',
        'firstname',
        'patronomic',
        'birthday',
        'position',
        'is_active',
    ]
    list_display_links = [
        'lastname',
        'firstname',
        'patronomic',
    ]
    search_fields = [
        'lastname',
        'firstname',
        'birthday',
    ]


admin.site.register(Resume, ResumeAdmin)
