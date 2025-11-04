from rest_framework import serializers
from .models import Sale, SaleItem

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['product', 'quantity', 'unit_price']

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['id', 'customer', 'employee', 'sale_date', 'total_amount', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sale = Sale.objects.create(**validated_data)
        total_amount = 0
        for item_data in items_data:
            SaleItem.objects.create(sale=sale, **item_data)
            total_amount += item_data['quantity'] * item_data['unit_price']
        sale.total_amount = total_amount
        sale.save()
        return sale
