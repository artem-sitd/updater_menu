from django.urls import path

from .views import CategoryDetail

app_name = "menu"

urlpatterns = [
    path("<slug:slug>/", CategoryDetail.as_view(), name="category_detail"),
]