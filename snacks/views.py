from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_home = "home.html"
    template_about = "about.html"
