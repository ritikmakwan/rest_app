from rest_framework import viewsets
from .models import Emp
from .Serializers import EmpSerializer
class EmpViewset(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer