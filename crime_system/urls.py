from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views  # un app peru core na idhu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # root url
    path('home/', views.home, name='home_page'),  # name change pannen
    path('report/', views.report_crime, name='report_crime'),
    path('crime/<int:crime_id>/', views.crime_detail, name='crime_detail'),
    path('crime/<int:crime_id>/edit/', views.edit_crime, name='edit_crime'),
    path('crime/<int:crime_id>/delete/', views.delete_crime, name='delete_crime'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]