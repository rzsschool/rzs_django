import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe
from tinymce.models import HTMLField


class TypeOfSocialNetwork(models.Model):
    class Meta:
        verbose_name_plural = "Види соціальних мереж"

    name = models.CharField(max_length=32, verbose_name='назва', unique=True)
    class_name = models.CharField(
        max_length=32,
        help_text='назви класів шукайте за посиланням https://fortawesome.com/sets/font-awesome-5-brands or https://fontawesome.com/',
        verbose_name="ім'я класу",
        unique=True,
    )

    def __str__(self):
        return self.name


class SocialNetworkOfUser(models.Model):
    class Meta:
        verbose_name_plural = "Соціальні мережі користувачів"

    type_of_social_network = models.ForeignKey(
        'TypeOfSocialNetwork',
        on_delete=models.CASCADE,
        verbose_name='Вид соціальної мережі'
    )
    link = models.CharField(max_length=255)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.type_of_social_network.name


class Person(models.Model):
    class Meta:
        verbose_name_plural = "Працівники"

    __SIZE_PHOTO = 80

    liberated = models.BooleanField(default=True, verbose_name='працює')

    # sex = models.CharField(
    #     max_length=36,
    #     choices=(
    #         ('woman', 'жіноча'),
    #         ('man', 'чоловіча'),
    #     ),
    #     verbose_name='стать'
    # )

    sex = models.SmallIntegerField(
        choices=(
            (0, 'жіноча'),
            (1, 'чоловіча'),
        ),
        verbose_name='стать'
    )

    lastname = models.CharField(max_length=32, verbose_name="прізвище")
    firstname = models.CharField(max_length=32, verbose_name="ім'я")
    patronymic = models.CharField(max_length=32, verbose_name="по батькові")

    photo = models.ImageField(
        upload_to='staff',
        verbose_name='фото',
        help_text='фото має бути розміром 300x300 px',
        # null=True,
        # blank=True
    )

    birthday = models.DateField()
    phone = models.CharField(max_length=16, null=True, blank=True, verbose_name='телефон')
    other_phone = models.CharField(max_length=16, null=True, blank=True, verbose_name='додатковий телефон')

    life_credo = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='Життєве кредо',
        # help_text=''
    )

    about_me = HTMLField(
        null=True,
        blank=True,
        verbose_name='Про себе',
        # help_text=''
    )

    def __str__(self):
        return self.get_initials()

    def get_initials(self):
        return f'{self.lastname} {self.firstname[0]}. {self.patronymic[0]}.'

    def get_fullname(self):
        return f'{self.lastname} {self.firstname} {self.patronymic}'


    @property
    def show_photo(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="{self.__SIZE_PHOTO}" height="{self.__SIZE_PHOTO}" />')
        return mark_safe(f'<img src="/static/img/user.png" width="{self.__SIZE_PHOTO}" height="{self.__SIZE_PHOTO}" />')


@receiver(models.signals.post_delete, sender=Person)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=Person)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = Person.objects.get(pk=instance.pk).photo
    except Person.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
