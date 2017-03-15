from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    name = models.CharField('Имя студента', max_length=2000)
    rating = models.IntegerField('Рейтинг', default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['name']