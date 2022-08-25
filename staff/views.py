from django.shortcuts import render, get_object_or_404

from .models import Person
from teachers.models import Lesson, Category
from administration.models import Administration
from teachers.models import Teacher
from other_staff.models import Category as CategoryOtherOfStaff


def staff(request):
    active_category = request.GET.get('cat', '')
    if not active_category:
        persons = Person.objects.filter(liberated=True).order_by('lastname')
    if active_category == 'Адміністрація':
        persons = [admin.person for admin in Administration.objects.order_by('person__lastname')]
    elif active_category == 'Вчителі':
        persons = [teacher.person for teacher in Teacher.objects.order_by('person__lastname')]
    elif active_category:
        persons = []
        cat = CategoryOtherOfStaff.objects.filter(name=active_category).first()
        if not cat:
            cat = CategoryOtherOfStaff.objects.filter(names=active_category).first()
        if cat:
            persons = [other_staff.person for other_staff in cat.otherstaff_set.all().order_by('person__lastname')]

    context = {
        'persons': persons,
        'active_category': active_category,
        'cat_other_staff': CategoryOtherOfStaff.objects.order_by('name'),
    }
    return render(request, 'staff/staff.html', context=context)


def staff_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)

    info_about_teacher = None
    if hasattr(person, 'teacher'):
        teacher_category = person.teacher.categories
        teacher_ranks = ', '.join(map(str, person.teacher.ranks.all()))
        info_about_teacher = f'{teacher_category}, {teacher_ranks}' if teacher_ranks else teacher_category

    context = {
        'person': person,
        'info_about_teacher': info_about_teacher,
        'certificates': person.certificate_set.order_by('-date'),
        'lessons': Lesson.objects.order_by('name'),
        'categories': Category.objects.order_by('-mass'),
    }
    return render(request, 'staff/single.html', context=context)
