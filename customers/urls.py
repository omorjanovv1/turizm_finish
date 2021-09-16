from django.urls import path
from .views import (index, tours, get_detail, tour_registration,
                    tour_registration_success, already_registered,
                    TourRegistrationDeleteView)

urlpatterns = [
    path('', index, name="index"),
    path('tours/', tours, name='tours'),
    path('detail/<int:id>/', get_detail, name='detail'),
    path('tour/registration/', tour_registration, name='tour_registration'),
    path('tour/registration/done', tour_registration_success, name='success'),
    path('tour/registration/already', already_registered, name='already'),
    path('delete/<int:pk>/', TourRegistrationDeleteView.as_view(), name='delete'),
]
