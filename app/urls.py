from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index,name='index'),
    path('', views.login, name='login'),
    path('register/', views.register),
    path('logout/', views.logout),
    path('picture/', views.picture, name='picture'),
    path('video/', views.video, name='video'),
    path('upload/', views.upload),
    path('stylize/<type>', views.stylize, name='stylize'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)