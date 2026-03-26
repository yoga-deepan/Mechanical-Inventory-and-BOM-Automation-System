from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BOMItem, StockTransaction

@receiver(post_save, sender=BOMItem)
def deduct_stock_on_bom_creation(sender, instance, created, **kwargs):
    """
    Automatically deduct stock when BOM item is created
    and create audit trail
    """
    if created:
        component = instance.component
        quantity = instance.quantity_required
        
        # Deduct stock
        component.current_stock -= quantity
        component.save()
        
        # Create transaction record
        StockTransaction.objects.create(
            component=component,
            quantity_changed=quantity,
            transaction_type='USED',
            note=f'Used in project: {instance.project.name}'
        )
