from django.db import models

from staff.models import Person


class TypeOfAdministrativePosition(models.Model):
    class Meta:
        verbose_name_plural = 'Види адміністративної посади'

    type_position = models.CharField(
        max_length=64,
        verbose_name='посада',
        help_text='приклад: Директор гімназії | Заступник директора з навчально-виховної роботи...',
        unique=True,
    )
    # is_boss = models.Model()

    def __str__(self):
        return self.type_position


class Administration(models.Model):
    class Meta:
        verbose_name_plural = 'Адміністрація'

    position = models.ForeignKey(
        TypeOfAdministrativePosition,
        on_delete=models.CASCADE,
        verbose_name='посада'
    )

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        verbose_name='працівник',
    )

    def __str__(self):
        return self.person.get_fullname()
