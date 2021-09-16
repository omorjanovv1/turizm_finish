from django.shortcuts import render, redirect
from .models import Tour, TourRegistration
from .forms import TourForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html', locals())


def tours(request):
    posts = Tour.objects.all()
    posts2 = Tour.objects.all().order_by('-id')
    if 'page' in request.GET:
        page = request.GET['page']
    else:
        page = 1
    paginator = Paginator(posts, 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'customers/tours.html', locals())


def get_detail(request, id):
    detail = Tour.objects.get(pk=id)
    print('islan')
    print(dir(detail))
    return render(request, 'customers/tour_detail.html', locals())


@login_required
def tour_registration(request):
    # current_user = request.user
    registered_tours = TourRegistration.objects.filter(user_name=request.user)

    if request.method == "POST":
        form = TourForm(request.POST)
        tour_again = registered_tours.filter(tour=form.data['tour'])
        if tour_again:
            return redirect('already')
        if form.is_valid():
            new_registration = form.save(commit=False)
            new_registration.user_name = request.user
            new_registration.save()
            return redirect('success')
    else:
        form = TourForm()

    return render(request, 'customers/tour_registration.html', locals())


def tour_registration_success(request):
    return render(request, 'customers/registration_done.html', locals())


def already_registered(request):
    return render(request, 'customers/already_registered.html', locals())


class TourRegistrationDeleteView(generic.DeleteView):
    model = TourRegistration
    template_name = 'customers/delete.html'
    success_url = reverse_lazy('registration:cabinet')
