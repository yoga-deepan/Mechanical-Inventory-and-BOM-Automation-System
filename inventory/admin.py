from django.contrib import admin
from .models import Component, Project, BOMItem, StockTransaction

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'material', 'current_stock', 'min_stock_level', 'is_low_stock']
    list_filter = ['category', 'unit_type']
    search_fields = ['name', 'material', 'supplier_name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'client_name', 'status', 'start_date', 'deadline']
    list_filter = ['status']
    search_fields = ['name', 'client_name']

@admin.register(BOMItem)
class BOMItemAdmin(admin.ModelAdmin):
    list_display = ['project', 'component', 'quantity_required', 'total_cost', 'total_weight']
    list_filter = ['project']

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ['component', 'quantity_changed', 'transaction_type', 'timestamp']
    list_filter = ['transaction_type', 'timestamp']
    readonly_fields = ['timestamp']
