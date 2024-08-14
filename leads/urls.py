from django.urls import path
from leads.views import home

app_name = "leads"

urlpatterns = [
    path('', home)
]