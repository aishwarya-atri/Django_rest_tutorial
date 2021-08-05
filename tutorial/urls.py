"""Tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include
# from snippets import urls
# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns([
#     path('', urls.api_root),
#     path('snippets/', urls.snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', urls.snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', urls.snippet_highlight, name='snippet-highlight'),
#     path('users/', urls.user_list, name='user-list'),
#     path('users/<int:pk>/', urls.user_detail, name='user-detail')
# ])

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]