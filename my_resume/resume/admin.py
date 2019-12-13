from django.contrib import admin


from .models import Resume

class ResumeAdmin(admin.ModelAdmin):

    list_display = ['lastname', 'firstname', 'patronomic', 'birthday', 'is_active']
    list_display_links = ['lastname', 'firstname', 'patronomic']
    search_fields = ['lastname', 'firstname', 'birthday']

admin.site.register(Resume, ResumeAdmin)

