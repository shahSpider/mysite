from django.urls import path
from leads.views import leads_list, leads_detail

app_name = "leads"

urlpatterns = [
    path('', leads_list),
    path('<pk>/', leads_detail)
]