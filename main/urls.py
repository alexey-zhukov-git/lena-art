"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

app_name = 'main'

from django.urls import path
from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('product-list/<slug:category_slug>/', product_list_by_category, name='product_list_by_category'),
    path('product-detail/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
]