from django.db import models

from staff.models import Person


class Lesson(models.Model):
    class Meta:
        verbose_name_plural = 'Уроки'

    name = models.CharField(max_length=64, unique=True, verbose_name="назва", help_text='приклад: математика')

    genitive_case_of_name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name="родовий відмінок",
        help_text='приклад: математики'
    )

    def __str__(self):
        return self.genitive_case_of_name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категорії'

    name = models.CharField(max_length=64, unique=True, verbose_name="назва")

    mass = models.SmallIntegerField(
        default=0,
        unique=True,
        verbose_name='ранг',
        help_text='ранг має бути унікальним для кожногї категорії'
    )

    def __str__(self):
        return self.name


class Rank(models.Model):
    class Meta:
        verbose_name_plural = 'Звання'

    name = models.CharField(max_length=64, unique=True, verbose_name="назва")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    class Meta:
        verbose_name_plural = 'Вчителі'

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        verbose_name='Працівник',
    )

    lessons = models.ManyToManyField(Lesson, verbose_name="уроки", blank=True)

    categories = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="категорія")

    ranks = models.ManyToManyField(
        Rank,
        blank=True,
        verbose_name="звання"
    )

    def __str__(self):
        return self.person.get_fullname()
