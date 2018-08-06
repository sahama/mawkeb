from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Zaer


# @login_required

def zaer_list(request):

    page = request.GET.get('page', 1)
    paginator = Paginator(Zaer.objects.all()[::-1], 100)

    try:
        zaers = paginator.page(page)
    except PageNotAnInteger:
        zaers = paginator.page(1)
    except EmptyPage:
        zaers = paginator.page(paginator.num_pages)

    context = {"zaers": zaers}
    return render(request, "zaer/list.html", context)


def zaer_detail(request, zaer_id):

    zaer = Zaer.objects.get(pk=zaer_id)

    context = {"zaer": zaer}
    return render(request, "zaer/detail.html", context)

def zaer_card(request, zaer_id):
    pass

