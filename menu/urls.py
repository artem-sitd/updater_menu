from django.urls import path

# from .views import get_main, get_about, get_contacts, get_history, get_portfolio, get_team, category_detail
from .views import CategoryDetail

app_name = "menu"

urlpatterns = [
    path("<slug:slug>/", CategoryDetail.as_view(), name="category_detail"),
]

