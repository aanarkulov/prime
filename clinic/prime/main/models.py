from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from embed_video.fields import EmbedVideoField
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _

from .utils import base_slugify

# Create your models here.

__all__ = ['Treatment']

class About(models.Model):
    about = models.TextField(help_text=_('О клинике'), verbose_name='О клинике')
    youtube_vid = EmbedVideoField(verbose_name=_('Видео на ютубе'), help_text=_('Например: https://www.youtube.com/watch?v=oBT4FR84PSg'))
    vision = models.TextField(verbose_name=_('Видение'))
    mission = models.TextField(verbose_name=_('Миссия'))
    philosophy = models.TextField(verbose_name=_('Наша философия'))

    def __str__(self):
        return "{}".format(self.about)

class Team(models.Model):
    fullname = models.CharField(max_length=120, help_text=_('Фамилия, Имя, Отчество'), verbose_name=_('ФИО'))
    specialty = models.CharField(max_length=120, help_text=_('Должность'), verbose_name=_('Напишите его должность'))
    about = models.TextField(verbose_name=_('Видение'))
    image = models.ImageField(upload_to='team', 
        null=True, 
        blank=True,
    )

    def __str__(self):
        return "{}".format(self.fullname)

class Contact(models.Model):
    address = models.CharField(max_length=255, verbose_name=_('Адрес'))
    telephones = models.CharField(max_length=120, help_text=_('Напишите все номера через запитой, например: 996 702 12-34-56, 996 702 12-34-56'), verbose_name='Номер телефона')
    email = models.EmailField(max_length=120, verbose_name='E-mail')

    def __str__(self):
        return "{}".format(self.address)

class Social(models.Model):
    link = models.CharField(max_length=60)
    symbol = models.CharField(max_length=13, help_text=_("Доступные соцети:")+" facebook, instagram, youtube")

    def __str__(self):
        return "{link}".format(link=self.link)

class Treatment(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('Название'))
    slug = models.SlugField(unique=True, null=False, default='')
    body = models.TextField(verbose_name='Описание')
    treatment_inner = models.TextField(verbose_name=_('Что входит в эту услугу:'))

    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    image = models.ImageField(upload_to='treatments', 
        null=True, 
        blank=True,
    )

    def save(self):
        super(Treatment, self).save()
        title = self.title
        self.slug = '{instance}'.format(
            instance=base_slugify(title)
        )
        super(Treatment, self).save()

    def __str__(self):
        return "{}".format(self.title)

class CategoryDiagnostica(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('Категория'))
    slug = models.SlugField(unique=True, null=False)

    def save(self):
        super(CategoryDiagnostica, self).save()
        name = self.name
        self.slug = '{instance}'.format(
            instance=base_slugify(name)
        )
        super(CategoryDiagnostica, self).save()

    def __str__(self):
        return '{name}'.format(name=self.name)

class UnderCategoryDiagnostica(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('По категория'))
    slug = models.SlugField(unique=True, null=False)
    category = models.ForeignKey(CategoryDiagnostica,on_delete=models.CASCADE, verbose_name=_('Категория'))

    def save(self):
        super(UnderCategoryDiagnostica, self).save()
        name = self.name
        self.slug = '{instance}'.format(
            instance=base_slugify(name)
        )
        super(UnderCategoryDiagnostica, self).save()

    def __str__(self):
        return '{name}'.format(name=self.name)

class Diagnostic(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('Название'))
    slug = models.SlugField(unique=True, null=False)
    body = models.TextField(verbose_name='Описание')
    diag_inner = models.TextField(verbose_name=_('Что входит в эту услугу:'))
    diag_more = models.TextField(verbose_name=_('При проведении:'))

    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    category = models.ForeignKey(CategoryDiagnostica, on_delete=models.PROTECT, verbose_name=_('Категория'))

    image = models.ImageField(upload_to='diagnostics', 
        null=True, 
        blank=True,
    )

    def save(self):
        super(Diagnostic, self).save()
        title = self.title
        self.slug = '{instance}'.format(
            instance=base_slugify(title)
        )
        super(Diagnostic, self).save()

    def __str__(self):
        return "{}".format(self.title)

# def pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
# pre_save.connect(pre_save_receiver, sender=Treatment)