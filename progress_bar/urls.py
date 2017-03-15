from django.conf.urls import url
from django.contrib import admin

from achievement import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.StudentsListView.as_view(), name='students_list'),
]
