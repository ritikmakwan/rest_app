from rest_framework import serializers
from .models import Emp,Products
class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = "__all__"
        

class ProductsSerializres(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"