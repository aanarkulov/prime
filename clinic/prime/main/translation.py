from modeltranslation.translator import TranslationOptions, register
from .models import About, Team, Contact, Treatment, CategoryDiagnostica, UnderCategoryDiagnostica, Diagnostic

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('about','vision', 'mission', 'philosophy', )

@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('fullname','specialty', 'about', )

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address', )

@register(Treatment)
class TreatmentTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'treatment_inner',)

@register(Diagnostic)
class DiagnosticTranslationOptions(TranslationOptions):
    fields = ('title','body','diag_inner', 'diag_more',)

@register(CategoryDiagnostica)
class CategoryDiagnosticaTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(UnderCategoryDiagnostica)
class UnderCategoryDiagnosticaTranslationOptions(TranslationOptions):
    fields = ('name',)