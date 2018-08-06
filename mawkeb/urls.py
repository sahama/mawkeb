"""mawkeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path
from zaer import views as zaer_view
from mawkeb import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', zaer_view.zaer_list, name='zaer_list'),
    path('<int:zaer_id>', zaer_view.zaer_detail, name='zaer_detail'),
    path('<int:zaer_id>/print', zaer_view.zaer_cart, name='zaer_cart'),
    path('<int:zaer_id>/out', zaer_view.zaer_set_out, name='zaer_out'),
    path('new/', zaer_view.zaer_new, name='zaer_new'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
