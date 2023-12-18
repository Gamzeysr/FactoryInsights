from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

routers = DefaultRouter()
routers.register("factory", FactoryView)
routers.register("machine", MachineView)


urlpatterns = [


]
urlpatterns += routers.urls
