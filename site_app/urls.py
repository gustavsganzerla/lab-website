from django.urls import path
from . import views

app_name = "site_app"

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('research/', views.research, name = 'research'),
    path('publications/', views.publications, name = 'publications')
]
