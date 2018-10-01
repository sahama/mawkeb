from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from .models import Zaer
from .form import ZaerForm
import datetime
import base64

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


def zaer_cart(request, zaer_id):
    zaer = Zaer.objects.get(pk=zaer_id)

    context = {"zaer": zaer}
    return render(request, "zaer/cart.html", context)

def zaer_set_out(request, zaer_id):
    zaer = Zaer.objects.get(pk=zaer_id)
    zaer.out_datetime = datetime.datetime.now()
    zaer.save()
    return redirect('zaer_detail', zaer_id)


@login_required
@transaction.atomic
def zaer_new(request):
    if request.method == 'POST':
        zaer = Zaer()
        form = ZaerForm(request.POST, request.FILES, instance=zaer)
        img_b64 = request.POST.get('image')
        img_b64 = img_b64.split(',', maxsplit=1)[1]
        img_bin = base64.b64decode(img_b64)


        if form.is_valid():
            form.save()
            content = ContentFile(img_bin)
            form.instance.image.save("{0}.png".format(form.instance.id), content)
            messages.success(request, 'new zaer!')
            return redirect('zaer_detail', zaer.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ZaerForm()

    return render(request, 'zaer/new.html', {
        'form': form,
    })


@login_required
def zaer_statistic(request):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    current_zaer = Zaer.objects.filter(out_datetime__gte=today).count()
    today_zaer = Zaer.objects.filter(in_datetime__day=today.day).count()
    yesterday_zaer = Zaer.objects.filter(in_datetime__day=yesterday.day).count()
    context = {
        "current_zaer": current_zaer,
        "today_zaer": today_zaer,
        "yesterday_zaer": yesterday_zaer
    }

    return render(request, "zaer/statistic.html", context)