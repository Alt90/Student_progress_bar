from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from achievement import views
from progress_bar import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.StudentsListView.as_view(), name='students_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
