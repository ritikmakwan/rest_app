from rest_framework import viewsets
from .models import Emp,Products
from .Serializers import EmpSerializer,ProductsSerializres
class EmpViewset(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    
class ProductsViewsets(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializres