from django.shortcuts import render, get_object_or_404

from pages.models import Page


def page(request, relative_link):
    obj_page = get_object_or_404(Page, relative_link=relative_link)
    return render(request, 'pages/page.html', context={
        'body': obj_page.body
    })
