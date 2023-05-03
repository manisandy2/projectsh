from rest_framework.routers import DefaultRouter
# from .views import BasicInformationList,BasicInformationDetail,api_root
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

# register_list = RegisterView.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# router = DefaultRouter()
# router.register("Basic_Information/",Basic_Information_List,basename="information_list"),
# router.register("Basic_Information/<int:pk>/",Basic_Information_Detail,basename="information_details")
#
# router = DefaultRouter()
# router.register(r'register', RegisterView.as_view(), basename="register")
# router.register(r'basic', BasicInformationView.as_view(), basename="basic")


urlpatterns = [
    path('register', BasicInformationList.as_view(),name="register"),
    path('register/<int:pk>', BasicInformationDetail.as_view(),name="register"),


]

# urlpatterns = router.urls




# RegisterDetail = RegisterDetail.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
#
# BasicInformationView = BasicInformationView.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# user_list = BasicInformationDetail.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
