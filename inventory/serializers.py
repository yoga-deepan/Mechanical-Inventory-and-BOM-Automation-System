from rest_framework import serializers
from .models import Component, Project, BOMItem, StockTransaction


class ComponentSerializer(serializers.ModelSerializer):
    is_low_stock = serializers.ReadOnlyField()
    
    class Meta:
        model = Component
        fields = '__all__'


class BOMItemSerializer(serializers.ModelSerializer):
    component_name = serializers.CharField(source='component.name', read_only=True)
    component_category = serializers.CharField(source='component.category', read_only=True)
    total_cost = serializers.ReadOnlyField()
    total_weight = serializers.ReadOnlyField()
    
    class Meta:
        model = BOMItem
        fields = ['id', 'project', 'component', 'component_name', 
                  'component_category', 'quantity_required', 'total_cost', 'total_weight']


class ProjectSerializer(serializers.ModelSerializer):
    total_cost = serializers.ReadOnlyField()
    total_weight = serializers.ReadOnlyField()
    bom_items = BOMItemSerializer(source='bomitem_set', many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'


class StockTransactionSerializer(serializers.ModelSerializer):
    component_name = serializers.CharField(source='component.name', read_only=True)
    
    class Meta:
        model = StockTransaction
        fields = '__all__'
