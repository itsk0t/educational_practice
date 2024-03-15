from django.contrib.auth.models import User
from django.db import models
from documents.models import Documents


class Status(models.Model):
    title = models.CharField('Статус', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'


class Applications(models.Model):
    full_name = models.CharField('ФИО', max_length=256)
    date_birth = models.DateField('Дата рождения')
    passport_series = models.CharField('Серия паспорта', max_length=4)
    passport_number = models.CharField('Номер паспорта', max_length=6)
    phone = models.CharField('Номер телефона', max_length=11)
    address = models.CharField('Адрес проживания', max_length=256)
    document_id = models.ForeignKey(Documents, on_delete=models.CASCADE)
    files = models.FileField('Файл')
    comment = models.TextField('Комментарий')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


