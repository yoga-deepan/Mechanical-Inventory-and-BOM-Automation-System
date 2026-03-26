from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, F
from .models import Component, Project, BOMItem, StockTransaction
from .serializers import (
    ComponentSerializer, ProjectSerializer, 
    BOMItemSerializer, StockTransactionSerializer
)
from .tasks import check_low_stock


class ComponentViewSet(viewsets.ModelViewSet):
    """CRUD operations for components"""
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    
    def get_queryset(self):
        queryset = Component.objects.all()
        
        # Search by name
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        
        # Filter by category
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        
        # Filter by material
        material = self.request.query_params.get('material', None)
        if material:
            queryset = queryset.filter(material__icontains=material)
        
        return queryset


class ProjectViewSet(viewsets.ModelViewSet):
    """CRUD operations for projects"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        queryset = Project.objects.all()
        
        # Filter by status
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        # Sort by deadline
        sort = self.request.query_params.get('sort', None)
        if sort == 'deadline':
            queryset = queryset.order_by('deadline')
        
        return queryset


class BOMItemViewSet(viewsets.ModelViewSet):
    """CRUD operations for BOM items"""
    queryset = BOMItem.objects.all()
    serializer_class = BOMItemSerializer
    
    def get_queryset(self):
        queryset = BOMItem.objects.all()
        
        # Filter by project
        project_id = self.request.query_params.get('project_id', None)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        
        return queryset


@api_view(['GET'])
def analytics(request):
    """Analytics dashboard data"""
    
    # Cost distribution by category
    category_costs = Component.objects.values('category').annotate(
        total_cost=Sum(F('cost_per_unit') * F('current_stock'))
    )
    
    # Most used components
    most_used = BOMItem.objects.values('component__name').annotate(
        total_used=Sum('quantity_required')
    ).order_by('-total_used')[:10]
    
    # Low stock components
    low_stock_count = Component.objects.filter(
        current_stock__lte=F('min_stock_level')
    ).count()
    
    # Project statistics
    project_stats = {
        'total': Project.objects.count(),
        'planning': Project.objects.filter(status='PLANNING').count(),
        'in_progress': Project.objects.filter(status='IN_PROGRESS').count(),
        'completed': Project.objects.filter(status='COMPLETED').count(),
    }
    
    # Total inventory value
    total_inventory_value = sum(
        c.cost_per_unit * c.current_stock 
        for c in Component.objects.all()
    )
    
    return Response({
        'category_costs': list(category_costs),
        'most_used_components': list(most_used),
        'low_stock_count': low_stock_count,
        'project_stats': project_stats,
        'total_inventory_value': float(total_inventory_value),
    })


@api_view(['POST'])
def trigger_low_stock_check(request):
    """Manually trigger low stock check"""
    check_low_stock.delay()
    return Response({'message': 'Low stock check triggered'})
