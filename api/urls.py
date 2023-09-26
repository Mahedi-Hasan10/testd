from django.contrib import admin
from django.urls import path,include
from account.views import Register
urlpatterns = [
    path('accounts/', include('account.urls')),
]
