from rest_framework.routers import DefaultRouter
# from .views import BasicInformationList,BasicInformationDetail,api_root
from django.urls import path,include
from .views import *

urlpatterns = [
    path('register', BasicInformationList.as_view(),name="register"),
    path('register/<int:pk>', BasicInformationDetail.as_view(), name="register"),
    path('caste', CasteList.as_view(), name="caste"),
    path('caste/<int:pk>', CasteDetail.as_view(), name="caste"),
    path('subcaste', SubCasteList.as_view(), name="subcaste"),
    path('subcaste/<int:pk>', SubCasteDetail.as_view(), name="subcaste"),

]
