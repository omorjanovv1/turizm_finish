from django import forms
from django.db import models

from .models import TourRegistration

class TourForm(forms.ModelForm):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = TourRegistration
        fields = (
            'tour', 'customer', 'kol', 'phone_number',
        )


