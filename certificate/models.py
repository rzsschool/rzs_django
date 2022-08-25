from django.db import models
from staff.models import Person


class TypeDoc(models.Model):
    class Meta:
        verbose_name_plural = 'Тип документу'

    name = models.CharField(max_length=64, unique=True, verbose_name='Назва')

    def __str__(self):
        return self.name


class Platform(models.Model):
    class Meta:
        verbose_name_plural = 'Платформа'

    name = models.CharField(max_length=64, unique=True, verbose_name='Назва')

    link = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Сертифікати'

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='Працівник'
    )

    name = models.CharField(max_length=128, verbose_name='Назва')

    link = models.CharField(max_length=256)

    type_doc = models.ForeignKey(TypeDoc, models.CASCADE, verbose_name='Тип документу')

    platform = models.ForeignKey(
        Platform,
        models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Платформа',
    )

    number_of_hours = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Кількість годин'
    )

    date = models.DateField(verbose_name='Дата видачі')

    def __str__(self):
        return self.name

