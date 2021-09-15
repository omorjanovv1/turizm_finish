from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.contrib.auth import get_user_model
from customers.models import TourRegistration
from django.contrib.auth.decorators import login_required

User = get_user_model()


class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class IndexPageView(TemplateView):
    template_name = 'index.html'


# class UserCabinetView(LoginRequiredMixin, DetailView):
#     model = User
#     template_name = 'cabinet.html'

@login_required
def cabinet(request):
    object = request.user
    tours = TourRegistration.objects.filter(user_name=request.user)
    return render(request, 'cabinet.html', locals())
