from django.urls import path

from .views import (get_cons, get_design, get_mobile, get_serv, get_soft,
                    get_web)

app_name = "services"

urlpatterns = [
    path("", get_serv, name="services"),  # ок
    path("cons/", get_cons, name="cons"),  # ок
    path("design/", get_design, name="design"),  # ок
    path("mobile/", get_mobile, name="mobile"),  # ок
    path("soft/", get_soft, name="soft"),  # ок
    path("web/", get_web, name="web"),  # ок
]
