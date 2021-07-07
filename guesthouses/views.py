from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import GuestHouse
from . import forms

# Create your views here.
class HomeView(ListView):

    """HomeView Definition"""

    model = GuestHouse
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "guesthouses"

"""
def room_num(request):
    page = request.GET.get("page")
    room_list = GuestHouse.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    print("------------paginator시작---------------")
    print(vars(rooms.paginator.num_pages))
    return render(request, "guesthouses/guesthouse_list.html",  {})
    """


class Guesthouse_detail(DetailView):
    
    model = GuestHouse

class Search(View):
    def get(self, request):

        city = request.GET.get("city")
        print(city)

        if city:

            form = forms.Searchform(request.GET)

            if form.is_valid():
                city = form.cleaned_data.get("city")
                price = form.cleaned_data.get("price")
                signatures = form.cleaned_data.get("signature")

                filter_args={}

                filter_args["city__startswith"] = city

                if price is not None:
                    filter_args["price__lte"] = price

                print(filter_args)

                guesthouses = GuestHouse.objects.filter(**filter_args).order_by("-created")

                print(guesthouses)

                for signature in signatures:
                    guesthouses = guesthouses.filter(signature=signature)

                print(guesthouses)

                return render(request, "guesthouses/search.html", {"form": form, "guesthouses": guesthouses})
        
        
        else:
            form = forms.Searchform()

        return render(request,"guesthouses/search.html",{"form":form})