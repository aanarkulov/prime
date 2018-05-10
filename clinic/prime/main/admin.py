from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

from .models import About, Team, Contact, Social, Treatment, CategoryDiagnostica, UnderCategoryDiagnostica, Diagnostic

# Register your models here.

from django.conf import settings
from django.utils import translation

class AdminLocaleURLMiddleware:

    def process_request(self, request):
        if request.path.startswith('/admin'):
            request.LANG = getattr(settings, 'ADMIN_LANGUAGE_CODE', settings.LANGUAGE_CODE)
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG

class TeamAdmin(admin.ModelAdmin):
    model = Team

    # Get the image url
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:85px;height:85px;border-radius:50px;"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    exclude = ['fullname', 'about', 'specialty']

    list_display = ('fullname','image_tag',)

class AboutAdmin(admin.ModelAdmin):
    model = About
    exclude = ['about', 'vision', 'mission', 'philosophy']

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    exclude = ['address',]

class TreatmentAdmin(admin.ModelAdmin):
    model = Treatment
    exclude = ['title', 'body', 'treatment_inner', 'slug']

class DiagnosticAdmin(admin.ModelAdmin):
    model = Diagnostic
    exclude = ['title','body','diag_inner', 'diag_more', 'slug']

class UnderCategoryDiagnosticaAdmin(admin.ModelAdmin):
    model = UnderCategoryDiagnostica
    exclude = ['name','slug',]

class CategoryDiagnosticaAdmin(admin.ModelAdmin):
    model = CategoryDiagnostica
    exclude = ['name','slug']

admin.site.register(Social)
admin.site.register(Team, TeamAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Diagnostic, DiagnosticAdmin)
admin.site.register(CategoryDiagnostica, CategoryDiagnosticaAdmin)
admin.site.register(UnderCategoryDiagnostica, UnderCategoryDiagnosticaAdmin)