from django.urls import path
from .views import IndexView, SignupView, LocationSearchView, LocationDeleteView, CreateImageView, LogoutGetView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='weather/login.html'), name='login'),
    path('logout/', LogoutGetView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('search/', LocationSearchView.as_view(), name='location_search'),
    path('delete/<int:loc_id>/', LocationDeleteView.as_view(), name='location_delete'),
    path('create-image/', CreateImageView.as_view(), name='create_image'),
]