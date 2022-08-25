from django.db import models

from staff.models import Person


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категорії'

    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name="назва (однина)",
        help_text='Приклад: Психолог',
    )

    names = models.CharField(
        max_length=64,
        unique=True,
        verbose_name="назва (множина)",
        help_text='Приклад: Психологи',
    )

    def __str__(self):
        return self.name


class OtherStaff(models.Model):
    class Meta:
        verbose_name_plural = 'Інші працівники'

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        verbose_name='Працівник',
    )

    categories = models.ManyToManyField(Category, verbose_name="категорії")

    def __str__(self):
        return self.person.get_fullname()
