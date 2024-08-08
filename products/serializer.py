from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def validate_product_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Product price must be non-negative.")
        return value

    def validate_product_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Product stock must be non-negative.")
        return value
