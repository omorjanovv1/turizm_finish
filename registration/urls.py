from django.urls import path
from registration.views import CreateUserView, IndexPageView, cabinet

app_name = 'registration'

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('', IndexPageView.as_view(), name='index'),
    path('cabinet/', cabinet, name='cabinet'),

]