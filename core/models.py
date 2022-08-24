import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe
from tinymce.models import HTMLField


# def jsonfield_default_value():
#     JSON = [
#         {
#             'name': 'Головна',
#         },
#         {
#             'name': 'Новини',
#         }
#
#     ]
#     return JSON


# class Menu(models.Model):
#     class Meta:
#         verbose_name_plural = "Меню"
#
#     __TYPE_MENU = (
#         ('main_menu', 'головне меню'),
#         ('footer_menu_row1', 'меню підвалу 1-ша колонка'),
#         ('footer_menu_row2', 'меню підвалу 2-га колонка'),
#     )
#
#     type_menu = models.CharField(
#         max_length=64,
#         unique=True,
#         verbose_name='тип меню',
#         choices=__TYPE_MENU,
#     )
#     json = models.JSONField(
#         # default=jsonfield_default_value,
#         help_text="Для зручної роботи з JSON використовуйте JSONReader https://jsonformatter.org/"
#     )


class Alerts(models.Model):
    class Meta:
        verbose_name_plural = "Оголошення"

    __CLASS_NAME = (
        ('primary', 'primary'),
        ('secondary', 'secondary'),
        ('success', 'success'),
        ('danger', 'danger'),
        ('warning', 'warning'),
        ('info', 'info'),
        ('light', 'light'),
        ('dark', 'dark'),
    )

    title = models.CharField(max_length=128, verbose_name='заголовок')

    style = models.CharField(
        max_length=32,
        choices=__CLASS_NAME,
        verbose_name='стиль',
    )

    body = HTMLField(
        verbose_name='контент',
        help_text='для більш вражаючого ефекту використовуйте тег hr'
    )

    is_published = models.BooleanField(default=True, verbose_name='Публікувати')


class Facility(models.Model):
    class Meta:
        verbose_name_plural = "Зручності"

    __ICON = (
        ("flaticon-001-swing", "001-swing"),
        ("flaticon-002-bricks", "002-bricks"),
        ("flaticon-003-feeding-bottle", "003-feeding-bottle"),
        ("flaticon-004-balloons", "004-balloons"),
        ("flaticon-005-marker", "005-marker"),
        ("flaticon-006-spinning-top", "006-spinning-top"),
        ("flaticon-007-sandbox", "007-sandbox"),
        ("flaticon-008-tambourine", "008-tambourine"),
        ("flaticon-009-bib", "009-bib"),
        ("flaticon-010-slide", "010-slide"),
        ("flaticon-011-mat", "011-mat"),
        ("flaticon-012-kite", "012-kite"),
        ("flaticon-013-brush", "013-brush"),
        ("flaticon-014-blackboard", "014-blackboard"),
        ("flaticon-015-potty", "015-potty"),
        ("flaticon-016-apple", "016-apple"),
        ("flaticon-017-toy-car", "017-toy-car"),
        ("flaticon-018-ball", "018-ball"),
        ("flaticon-019-pencil", "019-pencil"),
        ("flaticon-020-rattle", "020-rattle"),
        ("flaticon-021-juice-box", "021-juice-box"),
        ("flaticon-022-drum", "022-drum"),
        ("flaticon-023-girl", "023-girl"),
        ("flaticon-024-shape-toy", "024-shape-toy"),
        ("flaticon-025-sandwich", "025-sandwich"),
        ("flaticon-026-paper-boat", "026-paper-boat"),
        ("flaticon-027-xylophone", "027-xylophone"),
        ("flaticon-028-kindergarten", "028-kindergarten"),
        ("flaticon-029-clock", "029-clock"),
        ("flaticon-030-crayons", "030-crayons"),
        ("flaticon-031-bell", "031-bell"),
        ("flaticon-032-book", "032-book"),
        ("flaticon-033-blocks", "033-blocks"),
        ("flaticon-034-popsicle", "034-popsicle"),
        ("flaticon-035-table", "035-table"),
        ("flaticon-036-boy", "036-boy"),
        ("flaticon-037-toys", "037-toys"),
        ("flaticon-038-locker", "038-locker"),
        ("flaticon-039-seesaw", "039-seesaw"),
        ("flaticon-040-puzzle", "040-puzzle"),
        ("flaticon-041-abacus", "041-abacus"),
        ("flaticon-042-synthesizer", "042-synthesizer"),
        ("flaticon-043-teddy-bear", "043-teddy-bear"),
        ("flaticon-044-scissors", "044-scissors"),
        ("flaticon-045-cookies", "045-cookies"),
        ("flaticon-046-bucket", "046-bucket"),
        ("flaticon-047-backpack", "047-backpack"),
        ("flaticon-048-paper-plane", "048-paper-plane"),
        ("flaticon-049-cutlery", "049-cutlery"),
        ("flaticon-050-fence", "050-fence"),
    )

    title = models.CharField(max_length=32, verbose_name='заголовок')

    class_name_icon = models.CharField(
        max_length=64,
        verbose_name="ім'я класу іконки",
        help_text="вигляд та ім'я класу дивись нижче",
        choices=__ICON,
    )
    description = models.CharField(max_length=256, verbose_name='опис')

    mass = models.SmallIntegerField(
        default=0,
        unique=True,
        verbose_name='позиція',
        help_text='позиція має бути унікальним для кожногї зручності'
    )

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Відгуки'

    __SIZE_PHOTO = 50

    name = models.CharField(
        max_length=32,
        verbose_name="ім'я",
        help_text="дотримуйтесь заздалегіть вибраного шаблону. Приклад: прізвище, ім'я або ім'я та по батькові"
    )
    profession = models.CharField(
        max_length=32,
        verbose_name="професія",
        null=True,
        blank=True,
        help_text="перше слово з маленької букви"
    )
    photo = models.ImageField(
        upload_to='testimonials',
        verbose_name='фото',
        help_text='фото має бути розміром 100x100 px'
    )
    text = models.CharField(
        max_length=256,
        verbose_name='відгук',
        help_text='всі відгуки мають місти однакову кількість слів для кращого дизайну'
    )

    @property
    def show_photo(self):
        if self.photo:
            return mark_safe(
                f'<img src="{self.photo.url}" width="{self.__SIZE_PHOTO}" height="{self.__SIZE_PHOTO}" />')
        return ""

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Testimonial)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=Testimonial)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = Testimonial.objects.get(pk=instance.pk).photo
    except Testimonial.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
