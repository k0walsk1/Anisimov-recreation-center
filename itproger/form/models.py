from django.db import models

class Articles(models.Model):
    SERVICE_CHOICES = [
        ('option1', 'Места для размещения'),
        ('option2', 'Путешествия'),
        ('option3', 'Pазвлечения'),
        ('option4', 'Игры')
    ]

    yslyga = models.CharField('Выберите услугу', max_length=10, choices=SERVICE_CHOICES)
    phone = models.CharField('Телефон', max_length=10)
    email = models.CharField('Почта', max_length=250)
    coment = models.TextField('Комментарий')

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'
