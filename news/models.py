import os

from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from staff.models import Person
from django.dispatch import receiver
from bs4 import BeautifulSoup

NUMBER_OF_CHARACTERS_PREVIOUS_NEWS = 200


class ImageOfPost(models.Model):
    class Meta:
        verbose_name_plural = 'Зображення для новин'

    __HEIGHT = 200
    __WEIGHT = 300

    image = models.ImageField(
        upload_to='image_of_post/%Y/%m',
        verbose_name='зображення',
        # help_text='фото має бути розміром 600x400 px',
    )

    news = models.ForeignKey(
        'News',
        on_delete=models.CASCADE,
        verbose_name='новина',
    )

    @property
    def show_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="{self.__WEIGHT}" height="{self.__HEIGHT}" />')
        return ""


@receiver(models.signals.post_delete, sender=ImageOfPost)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=ImageOfPost)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = ImageOfPost.objects.get(pk=instance.pk).image
    except ImageOfPost.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class Categories(models.Model):
    class Meta:
        verbose_name_plural = 'Категорії'

    __HEIGHT = 100
    __WEIGHT = 150

    name = models.CharField(
        max_length=64,
        verbose_name='назва',
        help_text='перше слово має бути з великої літери',
        unique=True,
    )
    image = models.ImageField(
        upload_to='categories',
        verbose_name='зображення',
        help_text='фото має бути розміром 600x400 px',
    )

    def __str__(self):
        return self.name

    @property
    def show_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="{self.__WEIGHT}" height="{self.__HEIGHT}" />')
        return ""


@receiver(models.signals.post_delete, sender=Categories)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Categories)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = Categories.objects.get(pk=instance.pk).image
    except Categories.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Новини'

    title = models.CharField(max_length=64, verbose_name='Заголовок')
    author = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        verbose_name='автор',
    )
    categories = models.ForeignKey(
        'Categories',
        on_delete=models.PROTECT,
        verbose_name='категорія',
    )
    # images
    content = HTMLField()
    date_created = models.DateField(verbose_name='Дата публікації')
    is_published = models.BooleanField(default=True, verbose_name='Публікувати')

    def __str__(self):
        return self.title[:20]

    def get_author(self):
        return self.author.get_initials()

    def preview_content(self):
        soup_text = BeautifulSoup(self.content, 'html.parser').text
        if len(soup_text) > NUMBER_OF_CHARACTERS_PREVIOUS_NEWS:
            return soup_text[:NUMBER_OF_CHARACTERS_PREVIOUS_NEWS] + '...'
        return soup_text
