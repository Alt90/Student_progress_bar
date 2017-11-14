from django.db import models

from achievement.models import Student


class Quiz(models.Model):
    name = models.CharField(max_length=1024)

    class Meta:
        db_table = 'quiz'


class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.PROTECT)
    text = models.TextField()
    answer_mode = models.CharField(choices=(('one', 'one'), ('several', 'several'), ('custom', 'custom')), max_length=500)

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.PROTECT)
    is_correct = models.BooleanField(default=False)
    text = models.CharField(max_length=1024)

    class Meta:
        db_table = 'answer'


class StudentQuizRating(models.Model):
    quiz = models.ForeignKey('Quiz')
    student = models.ForeignKey(Student)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer, null=True, blank=True)
    custom_answer = models.CharField(null=True, blank=True, max_length=1024)

    class Meta:
        db_table = 'student_quiz_rating'
