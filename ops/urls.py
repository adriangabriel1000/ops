from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from user.views import ProfileViewSet
from cycle import views as cycle_views

router = routers.DefaultRouter()
router.register('profileapi', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user/', include('user.urls')),
    path('manplan/', include('manplan.urls')),
    path('cycle', include('cycle.urls')),
    path('cycleAPI/', cycle_views.cycleAPI, name='cycleAPI'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/login.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('', include(router.urls), name='profileapi'),
]

urlpatterns += [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)