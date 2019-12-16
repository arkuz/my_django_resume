from datetime import date
from django.db import models


class Resume(models.Model):
    is_active = models.BooleanField(verbose_name='Активна?')
    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronomic = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=20, default='+70000000000', verbose_name='Телефон')
    email = models.EmailField(max_length=100, default='hello@example.com', verbose_name='E-mail')
    address = models.CharField(max_length=200, blank=True, verbose_name='Адрес')
    photo = models.FileField(blank=True, verbose_name='Фотография')
    position = models.CharField(max_length=200, blank=True, verbose_name='Позиция')
    about = models.TextField(blank=True, verbose_name='Обо мне')

    def calculate_age(self):
        today = date.today()
        born = self.birthday
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    age = property(calculate_age)

    def __repr__(self):
        return f'Resume: {self.lastname} {self.firstname}'

    def __str__(self):
        return f'{self.lastname} {self.firstname}'

    class Meta:
        verbose_name_plural = 'Резюме'
        verbose_name = 'Резюме'


class MoreContacts(models.Model):
    is_active = models.BooleanField(verbose_name='Активна?')
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    link = models.CharField(max_length=250, blank=True, verbose_name='Ссылка')
    i_text = models.CharField(max_length=200, blank=True, verbose_name='Текст тега i')
    icon_class = models.CharField(max_length=100, blank=True, verbose_name='Класс для иконки')
    resume = models.ForeignKey('Resume', null=True, on_delete=models.PROTECT, verbose_name='Резюме')

    def __repr__(self):
        return f'MoreContacts: {self.title}'

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Дополнительные контакты'
        verbose_name = 'Дополнительный контакт'
