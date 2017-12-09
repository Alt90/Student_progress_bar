from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from achievement import views
from progress_bar import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.StudentsListView.as_view(), name='students_list'),
    url(r'^raiting_reduce/(?P<student_id>\d+)$', views.raiting_reduce, name='raiting_reduce'),
    url(r'^(?P<pk>\d+)/$', views.StudentsGroupDetailView.as_view(), name='group_choose'),
    url(r'^raiting_add/(?P<student_id>\d+)/$', views.raiting_add, name='raiting_add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
