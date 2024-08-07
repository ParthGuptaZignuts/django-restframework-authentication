from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def validate_product_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Product name must be at least 3 characters long.")
        return value

    def validate_product_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Product price must be greater than zero.")
        return value

    def validate_product_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Product stock cannot be negative.")
        return value

    def validate(self, data):
        if data['product_stock'] == 0 and data['product_price'] > 100:
            raise serializers.ValidationError("Products with zero stock cannot have a price over 100.")
        return data