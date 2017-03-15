from django.views.generic import ListView

from achievement import models


class StudentsListView(ListView):
    model = models.Student