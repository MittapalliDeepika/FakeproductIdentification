"""
URL configuration for blockchain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from fakeproduct import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('manufacture/',views.manufacture,name='manufacture'),
    path('manufacture/login/',views.login,name='login'),
    path('manufacture/signup/',views.register,name='register'),
    path('manufacture/product_details/',views.product_details,name='product_details'),
    # path('users/',views.users,name='users'),
    path('logout/',views.logout,name='logout'),
    path('users/', views.upload_image, name='upload_image'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)