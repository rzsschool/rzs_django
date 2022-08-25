from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import News, Categories

COUNT_NEWS_OF_PAGE = 9


def blog(request):
    # print(dir(request))
    # print(request.COOKIES)
    # print(request.META)
    active_category = request.GET.get('cat', '')

    if active_category:
        news = News.objects.filter(categories__name=active_category).filter(is_published=True).order_by('-date_created')
    else:
        news = News.objects.filter(is_published=True).order_by('-date_created')
    paginator = Paginator(news, COUNT_NEWS_OF_PAGE)
    page_number = validator_of_positive_numbers(request.GET.get('page', '1'))

    page_obj = paginator.get_page(page_number)

    end_n = paginator.page_range.stop - 1
    if page_number > end_n:
        page_number = end_n

    class_first_page, class_last_page, list_of_pages = get_list_of_pages(page_number, end_n)
    context = {
        'news': page_obj.object_list,
        'categories': Categories.objects.all(),
        'active_category': active_category,
        'list_of_pages': list_of_pages,
        'class_first_page': class_first_page,
        'class_last_page': class_last_page,
        'page_number': page_number,
        'next_link': page_number + 1,
        'previous_link': page_number - 1,
    }
    return render(request, 'news/blog.html', context=context)


def blog_detail(request, pk):
    post = get_object_or_404(News, pk=pk)
    if post.number_of_views < 10 ** 6:
        post.number_of_views += 1
        post.save()
    images_of_post = post.imageofpost_set.all()
    count_image = images_of_post.count()
    related_posts = News.objects.filter(categories__name=post.categories).order_by('-date_created')[:4]
    context = {
        'post': post,
        'images_of_post': images_of_post,
        'count_image': count_image,
        'related_posts': [obj for obj in related_posts if obj.pk != post.pk],
        'list_range_count_image': list(range(1, count_image)),
        'categories': Categories.objects.order_by('name'),
    }

    return render(request, 'news/single.html', context=context)


def get_list_of_pages(active_n: int, end_n: int) -> tuple:
    """
    :param active_n: active number of page
    :param end_n: end number of page
    :return: first class name, last class name, list for render html
    get_list_of_pages(1, 3) == 'disabled', '', [1, 2, 3]
    get_list_of_pages(55, 100) == '', '', [1, 2, 0, 53, 54, 55, 56, 57, 0, 99, 100]
    """

    lst = []
    if active_n <= 5:
        [lst.append(n) for n in range(1, active_n)]
    else:
        lst.extend([1, 2, 0, active_n - 2, active_n - 1])

    if active_n + 5 >= end_n:
        [lst.append(n) for n in range(active_n, end_n + 1)]
    else:
        lst.extend([active_n, active_n + 1, active_n + 2, 0, end_n - 1, end_n])
    return (
        'disabled' if active_n == 1 else '',
        'disabled' if active_n == end_n else '',
        lst,
    )


def validator_of_positive_numbers(n: str) -> int:
    if len(set(n) - set('0123456789')) == 0:
        return int(n)
    return 1
