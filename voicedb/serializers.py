from rest_framework import serializers

from .models import Prices, Items

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Items

class NlpSerializer(serializers.ModelSerializer):
    item = serializers.CharField(source='item.item')
    class Meta:
        model = Prices
        fields = '__all__'

    # def create(self, validated_data):
    #     items_data = validated_data.pop('item')
    #     price = Prices.objects.create(**validated_data)
    #     for item_data in items_data:
    #         item_data, created = Items.objects.get_or_create(name=item_data['item'])
    #         price.item.add(item_data)
    #     return price
    
