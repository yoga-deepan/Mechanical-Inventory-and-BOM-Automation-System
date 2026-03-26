from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import F
from .models import Component

@shared_task
def check_low_stock():
    """
    Celery task to check for low stock components
    and send email alerts
    """
    low_stock_components = Component.objects.filter(
        current_stock__lte=F('min_stock_level')
    )
    
    if low_stock_components.exists():
        for component in low_stock_components:
            subject = f'Low Stock Alert: {component.name}'
            message = f"""
Low Stock Alert

Component: {component.name}
Category: {component.get_category_display()}
Current Stock: {component.current_stock} {component.get_unit_type_display()}
Minimum Level: {component.min_stock_level} {component.get_unit_type_display()}
Supplier: {component.supplier_name or 'Not specified'}

Please reorder immediately.

This is an automated alert from Mechanical ERP System.
            """
            
            # Send email
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send email for {component.name}: {str(e)}")
    
    return f"Checked {low_stock_components.count()} low stock items"
