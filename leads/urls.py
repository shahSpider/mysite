from django.urls import path
from leads.views import lead_list, lead_detail, lead_create, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path('', lead_list, name="lead-list"),
    path('<int:pk>/', lead_detail, name="lead-detail"),
    path('create/', lead_create, name="lead-create"),
    path('update/<int:pk>', lead_update, name="lead-update"),
    path('delete/<int:pk>', lead_delete, name="lead-delete")
]