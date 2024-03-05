from django.db import models


class Documents(models.Model):
    image = models.ImageField('Изображение', upload_to='images/')
    title = models.CharField('Название документа', max_length=128)
    body = models.TextField('Описание документа')
    deadline = models.CharField('Сроки выдачи', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
