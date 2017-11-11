from django.views.generic import ListView
from django.shortcuts import redirect, get_object_or_404

from achievement import models


class StudentsListView(ListView):
    model = models.Student


def raiting_add(request, student_id):
    if request.user.is_authenticated:
        student = get_object_or_404(models.Student, pk=student_id)
        if student.rating <= models.Student.MAX_RAITING - models.Student.STEP:
            student.rating += models.Student.STEP
            student.save()
    return redirect('/')

def raiting_reduce(request, student_id):
    if request.user.is_authenticated:
        student = get_object_or_404(models.Student, pk=student_id)
        if student.rating >= models.Student.MIN_RAITING + models.Student.STEP:
            student.rating -= models.Student.STEP
            student.save()
    return redirect('/')