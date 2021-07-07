from django.urls import path
from guesthouses import views as guesthouse_views

app_name = "core"

urlpatterns = [path("", guesthouse_views.HomeView.as_view(), name="home")]
