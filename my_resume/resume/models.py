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


class Works(models.Model):
    is_active = models.BooleanField(verbose_name='Активна?')
    company = models.CharField(max_length=150, blank=True, verbose_name='Компания')
    position = models.CharField(max_length=200, blank=True, verbose_name='Позиция')
    description = models.TextField(blank=True, verbose_name='Описание')
    period = models.CharField(max_length=250, blank=True, verbose_name='Период работы')
    resume = models.ForeignKey('Resume', null=True, on_delete=models.PROTECT, verbose_name='Резюме')

    def __repr__(self):
        return f'Works: {self.company} - {self.position}'

    def __str__(self):
        return f'{self.company} - {self.position}'

    class Meta:
        verbose_name_plural = 'Места работы'
        verbose_name = 'Место работы'


class Educations(models.Model):
    is_active = models.BooleanField(verbose_name='Активна?')
    univercity = models.CharField(max_length=200, blank=True, verbose_name='Учебное заведение')
    faculy = models.CharField(max_length=200, blank=True, verbose_name='Факультет')
    qualification = models.CharField(max_length=200, blank=True, verbose_name='Квалификация')
    period = models.CharField(max_length=250, blank=True, verbose_name='Период обучения')
    resume = models.ForeignKey('Resume', null=True, on_delete=models.PROTECT, verbose_name='Резюме')

    def __repr__(self):
        return f'Educations: {self.univercity} - {self.faculy}'

    def __str__(self):
        return f'{self.univercity} - {self.faculy}'

    class Meta:
        verbose_name_plural = 'Места учебы'
        verbose_name = 'Место учебы'


class Skills(models.Model):
    is_active = models.BooleanField(verbose_name='Активна?')
    description = models.TextField(blank=True, verbose_name='Описание')
    resume = models.ForeignKey('Resume', null=True, on_delete=models.PROTECT, verbose_name='Резюме')

    def __repr__(self):
        return f'Skills: {self.description}'

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name_plural = 'Навыки'
        verbose_name = 'Навык'


class SkillsIcon(models.Model):
    is_active = models.BooleanField(verbose_name='Активна?')
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    icon_class = models.CharField(max_length=100, blank=True, verbose_name='Класс для иконки')
    resume = models.ForeignKey('Resume', null=True, on_delete=models.PROTECT, verbose_name='Резюме')

    def __repr__(self):
        return f'SkillsIcon: {self.title}'

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Иконки навыков'
        verbose_name = 'Иконка навыка'


class Courses(models.Model):
    is_active = models.BooleanField(verbose_name='Активна?')
    organization = models.CharField(max_length=200, blank=True, verbose_name='Организация проводившая курсы')
    title = models.CharField(max_length=200, blank=True, verbose_name='Название курса')
    link = models.CharField(max_length=200, blank=True, verbose_name='Ссылка')
    description = models.TextField(blank=True, verbose_name='Описание')
    period = models.CharField(max_length=250, blank=True, verbose_name='Период обучения')
    resume = models.ForeignKey('Resume', null=True, on_delete=models.PROTECT, verbose_name='Резюме')

    def __repr__(self):
        return f'Courses: {self.organization} - {self.title}'

    def __str__(self):
        return f'{self.organization} - {self.title}'

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
