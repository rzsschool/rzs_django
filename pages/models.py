import os

from django.db import models
from tinymce.models import HTMLField
from django.utils.safestring import mark_safe
from django.dispatch import receiver


class Page(models.Model):
    class Meta:
        verbose_name_plural = 'Сторінки'

    name = models.CharField(max_length=64, unique=True, verbose_name='назава')
    relative_link = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='відносне посилання',
        help_text='посилання не має містити лише латинські літери, цифри та символ ніжнього підкреслення, приклад: video_gallery'
    )
    body = HTMLField(help_text='після створення сторінки не забудьте додати її в меню')


class ImageOfPage(models.Model):
    class Meta:
        verbose_name_plural = 'Зображення для сторінок'

    __WEIGHT = 300

    name = models.CharField(max_length=64, verbose_name='назава')

    image = models.ImageField(
        upload_to='image_of_page',
        verbose_name='зображення',
    )

    data = models.DateField(auto_now_add=True, verbose_name='Дата завантаження')

    @property
    def show_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="{self.__WEIGHT}" />')
        return ""

    def get_link(self):
        return self.image.url


@receiver(models.signals.post_delete, sender=ImageOfPage)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=ImageOfPage)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = ImageOfPage.objects.get(pk=instance.pk).image
    except ImageOfPage.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
