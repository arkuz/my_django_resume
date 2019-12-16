from django.contrib import admin
from .models import Resume, MoreContacts, Works, Educations


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


class EducationsInLine(admin.TabularInline):
    model = Educations

    list_display = [
        'univercity',
        'faculty',
    ]
    list_display_links = [
        'univercity',
        'faculty',
    ]
    search_fields = [
        'univercity',
        'faculty',
    ]


class ResumeAdmin(admin.ModelAdmin):
    inlines = [
        MoreContactsInLine,
        WorksInLine,
        EducationsInLine,
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
