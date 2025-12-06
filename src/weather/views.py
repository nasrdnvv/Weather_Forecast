from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.views.generic import ListView, TemplateView, FormView, DeleteView
from django.urls import reverse_lazy
from .models import Location
import requests
from django.conf import settings
from django.contrib.auth import logout


class WeatherMixin:
    def get_weather(self, city_name: str):
        api_key = settings.OPENWEATHER_API_KEY
        url = (
            f"http://api.openweathermap.org/data/2.5/weather?q={city_name}"
            f"&appid={api_key}&units=metric&lang=ru"
        )
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
        except requests.RequestException:
            return None

        data = resp.json()
        return {
            "name": data.get("name"),
            "temperature": data.get("main", {}).get("temp"),
            "description": data.get("weather", [{}])[0].get("description"),
        }
class LogoutGetView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

class IndexView(ListView, WeatherMixin):
    model = Location
    template_name = "weather/index.html"
    context_object_name = "locations"  # временно — для get_context_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weather_list = []
        for location in context.get("locations", []):
            weather = self.get_weather(location.name)
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


class LocationSearchView(TemplateView, WeatherMixin):
    template_name = "weather/index.html"

    def get(self, request, *args, **kwargs):
        query = request.GET.get("q", "").strip()
        if not query:
            return redirect("home")

        weather = self.get_weather(query)
        weather_list = []
        if weather:
            weather["from_db"] = False
            weather_list.append(weather)

        return render(request, self.template_name, {"weather_list": weather_list})

class LocationDeleteView(DeleteView):
    model = Location
    pk_url_kwarg = "loc_id"
    success_url = reverse_lazy("home")

class CreateImageView(TemplateView):
    template_name = "weather/create_image.html"