from .views import HomePageView
from django.urls import path

urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
    path("about/", HomePageView.as_veiw(), name="about")
]
