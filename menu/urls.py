from django.urls import path
from .views import get_main, get_about, get_contacts, get_history, get_portfolio, get_team

app_name = 'menu'

urlpatterns = [
    path("", get_main, name="main"),
    path("portfolio/", get_portfolio, name="portfolio"),
    path("about/", get_about, name="about"),
    path("contacts/", get_contacts, name="contacts"),
    path("history/", get_history, name="history"),
    path("team/", get_team, name="team"),

]
