import django, base64
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# Text's splitter into two equal parts
@register.filter
def splitword(paragraph):
    split = -((-len(paragraph))//2)
    return paragraph[:split], paragraph[split:]

@register.filter
def as_list(value):
    return value.split(',', 1)[0]

@register.filter
def strip_language(value):
    return value.replace('/'+django.utils.translation.get_language()+'/','')

@register.filter
def strip_body_list(text):
    strip_text = text.split('\n')
    return strip_text