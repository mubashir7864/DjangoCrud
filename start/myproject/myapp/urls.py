
from django.urls import path
from . import views


urlpatterns = [

    path('', views.myview.as_view() )
]
