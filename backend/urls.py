
from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('index', index),
    path('layout', layout),
    path('post', postNFT),
    path('userHome', userHome),
    path('userOrder', userOrder,name='orders'),
    path('', include('authentication.urls'))
]
