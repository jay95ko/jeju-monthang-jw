from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def view_404 (request, exception=None):
    return redirect(reverse("core:home"))
