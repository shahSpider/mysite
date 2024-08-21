from django.urls import path
from setup.views import home
from django.contrib.auth.views import LoginView, LogoutView
from setup.views import SignupView

app_name = "setup"

urlpatterns = [
    path('', home, name="home-page"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),

]