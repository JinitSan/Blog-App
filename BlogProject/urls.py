"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views

# redirects from our main project to apps
urlpatterns = [
    # make the blog app the default/home
    path('', include('blog.urls')),

    # second approach to redirect directly to the view instead of
    # doing it via the urls.py of the app (as done above)
    # so the alias is named here itself
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),

    # use Django's built-in views, but they need templates
    # as they only handle the backend logic
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # tell Django to use specified url in case of using user uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
