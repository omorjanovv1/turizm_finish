from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tour(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tour_date = models.DateTimeField()
    # image = models.ImageField(upload_to='media', null=True, blank=True)
    unexpired = models.BooleanField()

    @staticmethod
    def get_unexpired_tours():
        return Tour.objects.filter(
            unexpired=True
        )

    def __str__(self):
        return f"{self.name} - {self.tour_date}"


class TourRegistration(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
    customer = models.CharField(max_length=100, verbose_name='Имя')
    kol = models.PositiveSmallIntegerField(default=1)
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    user_name = models.ForeignKey(User, null=True, blank=True,
                                  on_delete=models.CASCADE, related_name='tourist')

    def __str__(self):
        return f"{self.tour}  Дата регистрации: {self.created_date}"


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    tour = models.ForeignKey(Tour, related_name='posts',
                             on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

    def __str__(self):
        return f"{self.image.url}"
