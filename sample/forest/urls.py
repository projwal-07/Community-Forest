
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('karyasamiti/',views.karyasamiti,name='karyasamiti'),
    path('salakarsamiti/',views.salakarsamiti,name='salakarsamiti'),
    path('lekhasamiti/',views.lekhasamiti,name='lekhasamiti'),
    path('tolesamiti/',views.tolesamiti,name='tolesamiti'),
    path('chetriyasamiti/',views.chetriyasamiti,name='chetriyasamiti'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)