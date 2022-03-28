from django.urls import path
from . import views

app_name = "celery"

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('send-email',views.SendEmail.as_view(),name='send-email')
]
