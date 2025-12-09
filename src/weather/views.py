from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.views.generic import ListView, TemplateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import Location, User

from rest_framework.viewsets import ModelViewSet
from .serializers import LocationSerializer, UserSerializer
from .services.weather_services import get_weather
from .services.location_services import search_location_weather

class IndexView(ListView):
    model = Location
    template_name = "weather/index.html"
    context_object_name = "locations"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weather_list = []
        for location in context.get("locations", []):
            weather = get_weather(location.name)
            if weather:
                weather["from_db"] = True
                weather_list.append(weather)
        context["weather_list"] = weather_list
        return context

class SignupView(FormView):
    template_name = "weather/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LogoutGetView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

class LocationSearchView(TemplateView):
    template_name = "weather/index.html"
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q", "")
        if not query:
            return redirect("home")
        weather_list = search_location_weather(query)
        return render(request, self.template_name, {"weather_list": weather_list})

class LocationDeleteView(DeleteView):
    model = Location
    pk_url_kwarg = "loc_id"
    success_url = reverse_lazy("home")

class CreateImageView(TemplateView):
    template_name = "weather/create_image.html"

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer