from django.urls import path
from . import views

app_name = "guesthouses"

urlpatterns = [
    path("<int:pk>", views.Guesthouse_detail.as_view(), name="detail"),
    path("search/", views.Search.as_view(), name="search")
]
