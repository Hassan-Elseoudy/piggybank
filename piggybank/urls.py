from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from core import views

from rest_framework import routers

from core.views import CategoryModelViewSet, TransactionModelViewSet

router = routers.SimpleRouter()
router.register(r'categories', CategoryModelViewSet, basename="category")
router.register(r'transactions', TransactionModelViewSet, basename="transaction")

urlpatterns = [
                  path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
                  path("login/", obtain_auth_token, name="token")
              ] + router.urls
