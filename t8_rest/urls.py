
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.Viewsets import EmpViewset
router = routers.DefaultRouter()
router.register(r'emps',EmpViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path("",include('home.urls'))
]
