from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    MAX_RAITING = 100
    MIN_RAITING = 0
    STEP = 10

    name = models.CharField('Имя студента', max_length=2000)
    rating = models.IntegerField('Рейтинг',
                                 default=MIN_RAITING,
                                 validators=[MaxValueValidator(MAX_RAITING), MinValueValidator(MIN_RAITING)])

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['name']