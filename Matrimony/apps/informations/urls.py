from rest_framework.routers import DefaultRouter
from .views import BasicInformationList,BasicInformationDetail
from django.urls import path


# router = DefaultRouter()
# router.register("Basic_Information/",Basic_Information_List,basename="information_list"),
# router.register("Basic_Information/<int:pk>/",Basic_Information_Detail,basename="information_details")
#


urlpatterns = [
    path('basic', BasicInformationList.as_view(),name="basic"),
    path('basic/<int:pk>', BasicInformationDetail.as_view(),name="base_details"),
]