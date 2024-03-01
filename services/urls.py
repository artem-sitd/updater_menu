from django.urls import path
from .views import get_cons

app_name = 'services'

urlpatterns = [
    path("", get_cons, name="cons"),

]
