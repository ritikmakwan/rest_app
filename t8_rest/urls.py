
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.Viewsets import EmpViewset,ProductsViewsets
router = routers.DefaultRouter()
router.register(r'emps',EmpViewset)

router.register(r'products',ProductsViewsets)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #path("",include('home.urls'))
]
