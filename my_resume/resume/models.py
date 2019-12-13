from django.db import models


class Resume(models.Model):
    is_active = models.BooleanField(verbose_name='Активна?')
    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronomic = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения')
    photo = models.FileField(blank=True, verbose_name='Фотография')

    def __repr__(self):
        return f'Resume: {self.lastname} {self.firstname}'

    def __str__(self):
        return f'{self.lastname} {self.firstname}'

    class Meta:
        verbose_name_plural = 'Резюме'
        verbose_name = 'Резюме'
