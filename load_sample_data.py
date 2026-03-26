"""
Sample Data Loader for Mechanical ERP
Run this script to populate the database with sample components and projects
Usage: python load_sample_data.py
"""

import os
import django
from decimal import Decimal
from datetime import date, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mechanical_erp.settings')
django.setup()

from inventory.models import Component, Project, BOMItem

def load_sample_data():
    print("Loading sample data...")
    
    # Clear existing data
    print("Clearing existing data...")
    BOMItem.objects.all().delete()
    Project.objects.all().delete()
    Component.objects.all().delete()
    
    # Create sample components
    print("Creating components...")
    
    components_data = [
        # Fasteners
        {
            'name': 'M8 Hex Bolt',
            'category': 'FASTENERS',
            'material': 'SS304',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.025'),
            'cost_per_unit': Decimal('0.50'),
            'supplier_name': 'ABC Fasteners Ltd',
            'current_stock': Decimal('500'),
            'min_stock_level': Decimal('100'),
        },
        {
            'name': 'M10 Hex Bolt',
            'category': 'FASTENERS',
            'material': 'SS304',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.045'),
            'cost_per_unit': Decimal('0.75'),
            'supplier_name': 'ABC Fasteners Ltd',
            'current_stock': Decimal('300'),
            'min_stock_level': Decimal('50'),
        },
        {
            'name': 'M8 Nut',
            'category': 'FASTENERS',
            'material': 'SS304',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.008'),
            'cost_per_unit': Decimal('0.25'),
            'supplier_name': 'ABC Fasteners Ltd',
            'current_stock': Decimal('800'),
            'min_stock_level': Decimal('150'),
        },
        
        # Bearings
        {
            'name': '6205 Deep Groove Bearing',
            'category': 'BEARINGS',
            'material': 'Chrome Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.150'),
            'cost_per_unit': Decimal('5.00'),
            'supplier_name': 'SKF Bearings',
            'current_stock': Decimal('50'),
            'min_stock_level': Decimal('10'),
        },
        {
            'name': '6206 Deep Groove Bearing',
            'category': 'BEARINGS',
            'material': 'Chrome Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.200'),
            'cost_per_unit': Decimal('6.50'),
            'supplier_name': 'SKF Bearings',
            'current_stock': Decimal('30'),
            'min_stock_level': Decimal('8'),
        },
        
        # Shafts
        {
            'name': '20mm EN8 Shaft',
            'category': 'SHAFTS',
            'material': 'EN8',
            'unit_type': 'METER',
            'weight_per_unit': Decimal('2.500'),
            'cost_per_unit': Decimal('15.00'),
            'supplier_name': 'Steel Suppliers Inc',
            'current_stock': Decimal('25'),
            'min_stock_level': Decimal('5'),
        },
        {
            'name': '25mm EN8 Shaft',
            'category': 'SHAFTS',
            'material': 'EN8',
            'unit_type': 'METER',
            'weight_per_unit': Decimal('3.850'),
            'cost_per_unit': Decimal('22.00'),
            'supplier_name': 'Steel Suppliers Inc',
            'current_stock': Decimal('15'),
            'min_stock_level': Decimal('3'),
        },
        
        # Sheet Metal
        {
            'name': 'MS Sheet 2mm',
            'category': 'SHEET_METAL',
            'material': 'Mild Steel',
            'unit_type': 'KG',
            'weight_per_unit': Decimal('1.000'),
            'cost_per_unit': Decimal('3.50'),
            'supplier_name': 'Metal Mart',
            'current_stock': Decimal('200'),
            'min_stock_level': Decimal('50'),
        },
        {
            'name': 'SS304 Sheet 1.5mm',
            'category': 'SHEET_METAL',
            'material': 'SS304',
            'unit_type': 'KG',
            'weight_per_unit': Decimal('1.000'),
            'cost_per_unit': Decimal('8.50'),
            'supplier_name': 'Metal Mart',
            'current_stock': Decimal('100'),
            'min_stock_level': Decimal('25'),
        },
        
        # Motors
        {
            'name': 'AC Motor 1HP 1440RPM',
            'category': 'MOTORS',
            'material': 'Aluminum Housing',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('8.500'),
            'cost_per_unit': Decimal('150.00'),
            'supplier_name': 'Electric Motors Co',
            'current_stock': Decimal('10'),
            'min_stock_level': Decimal('2'),
        },
        {
            'name': 'AC Motor 2HP 1440RPM',
            'category': 'MOTORS',
            'material': 'Aluminum Housing',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('12.500'),
            'cost_per_unit': Decimal('225.00'),
            'supplier_name': 'Electric Motors Co',
            'current_stock': Decimal('8'),
            'min_stock_level': Decimal('2'),
        },
        
        # Electronics
        {
            'name': 'Proximity Sensor NPN',
            'category': 'ELECTRONICS',
            'material': 'Plastic',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.050'),
            'cost_per_unit': Decimal('12.00'),
            'supplier_name': 'Automation Parts',
            'current_stock': Decimal('20'),
            'min_stock_level': Decimal('5'),
        },
        {
            'name': 'Limit Switch',
            'category': 'ELECTRONICS',
            'material': 'Plastic',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.080'),
            'cost_per_unit': Decimal('8.50'),
            'supplier_name': 'Automation Parts',
            'current_stock': Decimal('15'),
            'min_stock_level': Decimal('5'),
        },
        
        # Custom Machined Parts
        {
            'name': 'Custom Flange 100mm',
            'category': 'CUSTOM_MACHINED',
            'material': 'EN8',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('1.250'),
            'cost_per_unit': Decimal('45.00'),
            'supplier_name': 'Precision Machining',
            'current_stock': Decimal('12'),
            'min_stock_level': Decimal('3'),
        },
        {
            'name': 'Custom Coupling 25mm',
            'category': 'CUSTOM_MACHINED',
            'material': 'EN8',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.850'),
            'cost_per_unit': Decimal('35.00'),
            'supplier_name': 'Precision Machining',
            'current_stock': Decimal('8'),
            'min_stock_level': Decimal('2'),
        },
    ]
    
    components = []
    for data in components_data:
        component = Component.objects.create(**data)
        components.append(component)
        print(f"  ✓ Created: {component.name}")
    
    # Create sample projects
    print("\nCreating projects...")
    
    today = date.today()
    
    projects_data = [
        {
            'name': 'Hydraulic Press Assembly',
            'description': 'Design and assembly of 50-ton hydraulic press for metal forming operations',
            'client_name': 'ABC Manufacturing Ltd',
            'start_date': today - timedelta(days=30),
            'deadline': today + timedelta(days=60),
            'status': 'IN_PROGRESS',
        },
        {
            'name': 'Conveyor System Upgrade',
            'description': 'Upgrade existing conveyor system with new motors and sensors',
            'client_name': 'XYZ Industries',
            'start_date': today - timedelta(days=15),
            'deadline': today + timedelta(days=45),
            'status': 'PLANNING',
        },
        {
            'name': 'CNC Machine Retrofit',
            'description': 'Retrofit old CNC machine with new control system and motors',
            'client_name': 'Precision Tools Inc',
            'start_date': today - timedelta(days=90),
            'deadline': today - timedelta(days=10),
            'status': 'COMPLETED',
        },
    ]
    
    projects = []
    for data in projects_data:
        project = Project.objects.create(**data)
        projects.append(project)
        print(f"  ✓ Created: {project.name}")
    
    # Create sample BOM items
    print("\nCreating BOM items...")
    
    # Hydraulic Press Assembly BOM
    bom_items = [
        {'project': projects[0], 'component': components[0], 'quantity_required': Decimal('50')},   # M8 Bolts
        {'project': projects[0], 'component': components[2], 'quantity_required': Decimal('50')},   # M8 Nuts
        {'project': projects[0], 'component': components[3], 'quantity_required': Decimal('4')},    # Bearings
        {'project': projects[0], 'component': components[5], 'quantity_required': Decimal('2')},    # 20mm Shaft
        {'project': projects[0], 'component': components[7], 'quantity_required': Decimal('50')},   # MS Sheet
        {'project': projects[0], 'component': components[9], 'quantity_required': Decimal('1')},    # 1HP Motor
        
        # Conveyor System BOM
        {'project': projects[1], 'component': components[1], 'quantity_required': Decimal('30')},   # M10 Bolts
        {'project': projects[1], 'component': components[4], 'quantity_required': Decimal('8')},    # 6206 Bearings
        {'project': projects[1], 'component': components[10], 'quantity_required': Decimal('2')},   # 2HP Motor
        {'project': projects[1], 'component': components[11], 'quantity_required': Decimal('6')},   # Proximity Sensor
        {'project': projects[1], 'component': components[12], 'quantity_required': Decimal('4')},   # Limit Switch
        
        # CNC Machine Retrofit BOM
        {'project': projects[2], 'component': components[0], 'quantity_required': Decimal('40')},   # M8 Bolts
        {'project': projects[2], 'component': components[6], 'quantity_required': Decimal('1')},    # 25mm Shaft
        {'project': projects[2], 'component': components[10], 'quantity_required': Decimal('3')},   # 2HP Motor
        {'project': projects[2], 'component': components[13], 'quantity_required': Decimal('2')},   # Custom Flange
    ]
    
    for item_data in bom_items:
        bom_item = BOMItem.objects.create(**item_data)
        print(f"  ✓ Added {item_data['component'].name} to {item_data['project'].name}")
    
    print("\n" + "="*50)
    print("✅ Sample data loaded successfully!")
    print("="*50)
    print(f"\nCreated:")
    print(f"  • {len(components)} Components")
    print(f"  • {len(projects)} Projects")
    print(f"  • {len(bom_items)} BOM Items")
    print(f"\nYou can now:")
    print(f"  1. View dashboard at http://localhost:8000")
    print(f"  2. Browse components at http://localhost:8000/components/")
    print(f"  3. Check projects at http://localhost:8000/projects/")
    print(f"  4. View analytics at http://localhost:8000/analytics/")
    print()

if __name__ == '__main__':
    load_sample_data()
