from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('report/', views.report_crime, name='report_crime'),
    path('crime/<int:crime_id>/', views.crime_detail, name='crime_detail'), # <-- Ithu mukkiyam
    path('crime/<int:crime_id>/edit/', views.edit_crime, name='edit_crime'),
    path('crime/<int:crime_id>/delete/', views.delete_crime, name='delete_crime'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('', views.home), # root url
    path('',include('crime_app.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)