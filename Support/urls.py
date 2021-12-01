
from django.contrib import admin
from django.urls import path, include
from support_app import views
from .views import SupportView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', SupportView.as_view()),
    path('', views.index),

]
