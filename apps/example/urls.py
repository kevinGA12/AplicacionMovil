"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from django.urls import include, path, re_path
from apps.example import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

app_name = 'example'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Set log_in as the root URL
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'),

    # ... any other URLs ...
]
