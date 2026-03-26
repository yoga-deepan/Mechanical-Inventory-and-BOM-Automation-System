from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

class Component(models.Model):
    """Inventory Master - Stores all mechanical components"""
    
    CATEGORY_CHOICES = [
        ('FASTENERS', 'Fasteners'),
        ('BEARINGS', 'Bearings'),
        ('SHAFTS', 'Shafts'),
        ('SHEET_METAL', 'Sheet Metal'),
        ('MOTORS', 'Motors'),
        ('ELECTRONICS', 'Electronics'),
        ('CUSTOM_MACHINED', 'Custom Machined Parts'),
    ]
    
    UNIT_CHOICES = [
        ('NOS', 'Numbers'),
        ('KG', 'Kilograms'),
        ('METER', 'Meters'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    material = models.CharField(max_length=100, blank=True)
    unit_type = models.CharField(max_length=20, choices=UNIT_CHOICES, default='NOS')
    weight_per_unit = models.DecimalField(
        max_digits=10, 
        decimal_places=3,
        validators=[MinValueValidator(Decimal('0.001'))]
    )
    cost_per_unit = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    supplier_name = models.CharField(max_length=200, blank=True)
    current_stock = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0'))]
    )
    min_stock_level = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=10,
        validators=[MinValueValidator(Decimal('0'))]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.category})"
    
    @property
    def is_low_stock(self):
        return self.current_stock <= self.min_stock_level


class Project(models.Model):
    """Project Master - Tracks engineering projects"""
    
    STATUS_CHOICES = [
        ('PLANNING', 'Planning'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    client_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNING')
    created_at = models.DateTimeField(auto_now_add=True)
    components = models.ManyToManyField(Component, through='BOMItem')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    @property
    def total_cost(self):
        total = sum(
            item.component.cost_per_unit * item.quantity_required 
            for item in self.bomitem_set.all()
        )
        return total
    
    @property
    def total_weight(self):
        total = sum(
            item.component.weight_per_unit * item.quantity_required 
            for item in self.bomitem_set.all()
        )
        return total


class BOMItem(models.Model):
    """Bill of Materials Item - Links components to projects"""
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity_required = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    
    class Meta:
        unique_together = ['project', 'component']
    
    def __str__(self):
        return f"{self.project.name} - {self.component.name}"
    
    @property
    def total_cost(self):
        return self.component.cost_per_unit * self.quantity_required
    
    @property
    def total_weight(self):
        return self.component.weight_per_unit * self.quantity_required


class StockTransaction(models.Model):
    """Audit trail for inventory changes"""
    
    TRANSACTION_TYPES = [
        ('ADDED', 'Stock Added'),
        ('USED', 'Stock Used'),
    ]
    
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity_changed = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.transaction_type} - {self.component.name} - {self.quantity_changed}"
