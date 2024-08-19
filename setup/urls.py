from django.urls import path
from setup.views import home

app_name = "setup"

urlpatterns = [
    path('', home, name="home-page")
]