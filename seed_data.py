"""
Realistic Demo Data Generator for Mechanical ERP
Generates 30 components, 5 projects, and realistic BOM items
Usage: python seed_data.py
"""

import os
import django
from decimal import Decimal
from datetime import date, timedelta
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mechanical_erp.settings')
django.setup()

from inventory.models import Component, Project, BOMItem, StockTransaction

def clear_existing_data():
    """Clear all existing data"""
    print("🗑️  Clearing existing data...")
    BOMItem.objects.all().delete()
    StockTransaction.objects.all().delete()
    Project.objects.all().delete()
    Component.objects.all().delete()
    print("✅ Data cleared\n")

def create_components():
    """Create 30 realistic mechanical components"""
    print("🔩 Creating components...")
    
    components_data = [
        # FASTENERS (8 items)
        {
            'name': 'M6 Hex Bolt SS304',
            'category': 'FASTENERS',
            'material': 'SS304 Stainless Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.012'),
            'cost_per_unit': Decimal('0.35'),
            'supplier_name': 'Fasteners India Ltd',
            'current_stock': Decimal('800'),
            'min_stock_level': Decimal('150'),
        },
        {
            'name': 'M8 Hex Bolt Grade 8.8',
            'category': 'FASTENERS',
            'material': 'Alloy Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.025'),
            'cost_per_unit': Decimal('0.50'),
            'supplier_name': 'Fasteners India Ltd',
            'current_stock': Decimal('600'),
            'min_stock_level': Decimal('120'),
        },
        {
            'name': 'M10 Hex Bolt Grade 10.9',
            'category': 'FASTENERS',
            'material': 'High Tensile Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.045'),
            'cost_per_unit': Decimal('0.85'),
            'supplier_name': 'Fasteners India Ltd',
            'current_stock': Decimal('400'),
            'min_stock_level': Decimal('80'),
        },
        {
            'name': 'M6 Hex Nut SS304',
            'category': 'FASTENERS',
            'material': 'SS304',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.005'),
            'cost_per_unit': Decimal('0.20'),
            'supplier_name': 'Fasteners India Ltd',
            'current_stock': Decimal('1000'),
            'min_stock_level': Decimal('200'),
        },
        {
            'name': 'M8 Flat Washer',
            'category': 'FASTENERS',
            'material': 'Mild Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.003'),
            'cost_per_unit': Decimal('0.15'),
            'supplier_name': 'Fasteners India Ltd',
            'current_stock': Decimal('1200'),
            'min_stock_level': Decimal('250'),
        },
        {
            'name': 'Self Tapping Screw 4x25mm',
            'category': 'FASTENERS',
            'material': 'Hardened Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.008'),
            'cost_per_unit': Decimal('0.30'),
            'supplier_name': 'Fasteners India Ltd',
            'current_stock': Decimal('500'),
            'min_stock_level': Decimal('100'),
        },
        {
            'name': 'Socket Head Cap Screw M8',
            'category': 'FASTENERS',
            'material': 'Alloy Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.028'),
            'cost_per_unit': Decimal('1.20'),
            'supplier_name': 'Fasteners India Ltd',
            'current_stock': Decimal('300'),
            'min_stock_level': Decimal('60'),
        },
        {
            'name': 'Spring Washer M10',
            'category': 'FASTENERS',
            'material': 'Spring Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.006'),
            'cost_per_unit': Decimal('0.25'),
            'supplier_name': 'Fasteners India Ltd',
            'current_stock': Decimal('700'),
            'min_stock_level': Decimal('150'),
        },
        
        # BEARINGS (5 items)
        {
            'name': '608ZZ Ball Bearing',
            'category': 'BEARINGS',
            'material': 'Chrome Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.012'),
            'cost_per_unit': Decimal('15.00'),
            'supplier_name': 'SKF India',
            'current_stock': Decimal('80'),
            'min_stock_level': Decimal('20'),
        },
        {
            'name': '6204 Deep Groove Bearing',
            'category': 'BEARINGS',
            'material': 'Chrome Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.110'),
            'cost_per_unit': Decimal('85.00'),
            'supplier_name': 'SKF India',
            'current_stock': Decimal('45'),
            'min_stock_level': Decimal('10'),
        },
        {
            'name': '6205 Deep Groove Bearing',
            'category': 'BEARINGS',
            'material': 'Chrome Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.150'),
            'cost_per_unit': Decimal('120.00'),
            'supplier_name': 'SKF India',
            'current_stock': Decimal('35'),
            'min_stock_level': Decimal('8'),
        },
        {
            'name': 'Thrust Bearing 51204',
            'category': 'BEARINGS',
            'material': 'Chrome Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.065'),
            'cost_per_unit': Decimal('95.00'),
            'supplier_name': 'SKF India',
            'current_stock': Decimal('25'),
            'min_stock_level': Decimal('5'),
        },
        {
            'name': 'Linear Bearing LM8UU',
            'category': 'BEARINGS',
            'material': 'Chrome Steel',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.025'),
            'cost_per_unit': Decimal('45.00'),
            'supplier_name': 'SKF India',
            'current_stock': Decimal('60'),
            'min_stock_level': Decimal('15'),
        },
        
        # SHAFTS (4 items)
        {
            'name': 'Mild Steel Shaft 20mm',
            'category': 'SHAFTS',
            'material': 'EN8 Mild Steel',
            'unit_type': 'METER',
            'weight_per_unit': Decimal('2.466'),
            'cost_per_unit': Decimal('180.00'),
            'supplier_name': 'Steel Mart India',
            'current_stock': Decimal('30'),
            'min_stock_level': Decimal('5'),
        },
        {
            'name': 'Stainless Steel Shaft 25mm',
            'category': 'SHAFTS',
            'material': 'SS304',
            'unit_type': 'METER',
            'weight_per_unit': Decimal('3.853'),
            'cost_per_unit': Decimal('450.00'),
            'supplier_name': 'Steel Mart India',
            'current_stock': Decimal('20'),
            'min_stock_level': Decimal('4'),
        },
        {
            'name': 'Keyed Shaft 15mm EN8',
            'category': 'SHAFTS',
            'material': 'EN8',
            'unit_type': 'METER',
            'weight_per_unit': Decimal('1.387'),
            'cost_per_unit': Decimal('220.00'),
            'supplier_name': 'Steel Mart India',
            'current_stock': Decimal('25'),
            'min_stock_level': Decimal('5'),
        },
        {
            'name': 'Linear Shaft 8mm Hardened',
            'category': 'SHAFTS',
            'material': 'Hardened Steel',
            'unit_type': 'METER',
            'weight_per_unit': Decimal('0.395'),
            'cost_per_unit': Decimal('120.00'),
            'supplier_name': 'Steel Mart India',
            'current_stock': Decimal('40'),
            'min_stock_level': Decimal('10'),
        },
        
        # SHEET METAL (3 items)
        {
            'name': 'Aluminium Plate 5mm 6061',
            'category': 'SHEET_METAL',
            'material': 'Aluminium 6061',
            'unit_type': 'KG',
            'weight_per_unit': Decimal('1.000'),
            'cost_per_unit': Decimal('320.00'),
            'supplier_name': 'Metal Suppliers Co',
            'current_stock': Decimal('150'),
            'min_stock_level': Decimal('30'),
        },
        {
            'name': 'MS Sheet 3mm',
            'category': 'SHEET_METAL',
            'material': 'Mild Steel',
            'unit_type': 'KG',
            'weight_per_unit': Decimal('1.000'),
            'cost_per_unit': Decimal('65.00'),
            'supplier_name': 'Metal Suppliers Co',
            'current_stock': Decimal('250'),
            'min_stock_level': Decimal('50'),
        },
        {
            'name': 'SS304 Plate 4mm',
            'category': 'SHEET_METAL',
            'material': 'SS304',
            'unit_type': 'KG',
            'weight_per_unit': Decimal('1.000'),
            'cost_per_unit': Decimal('180.00'),
            'supplier_name': 'Metal Suppliers Co',
            'current_stock': Decimal('120'),
            'min_stock_level': Decimal('25'),
        },
        
        # MOTORS (4 items)
        {
            'name': '12V DC Motor 100RPM',
            'category': 'MOTORS',
            'material': 'Aluminum Housing',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.450'),
            'cost_per_unit': Decimal('280.00'),
            'supplier_name': 'Motors & Drives Ltd',
            'current_stock': Decimal('25'),
            'min_stock_level': Decimal('5'),
        },
        {
            'name': '24V DC Gear Motor 60RPM',
            'category': 'MOTORS',
            'material': 'Metal Gearbox',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.850'),
            'cost_per_unit': Decimal('650.00'),
            'supplier_name': 'Motors & Drives Ltd',
            'current_stock': Decimal('18'),
            'min_stock_level': Decimal('4'),
        },
        {
            'name': 'Stepper Motor NEMA17',
            'category': 'MOTORS',
            'material': 'Steel Frame',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.280'),
            'cost_per_unit': Decimal('450.00'),
            'supplier_name': 'Motors & Drives Ltd',
            'current_stock': Decimal('30'),
            'min_stock_level': Decimal('8'),
        },
        {
            'name': 'AC Motor 1HP 1440RPM',
            'category': 'MOTORS',
            'material': 'Cast Iron',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('8.500'),
            'cost_per_unit': Decimal('3200.00'),
            'supplier_name': 'Motors & Drives Ltd',
            'current_stock': Decimal('12'),
            'min_stock_level': Decimal('3'),
        },
        
        # ELECTRONICS (6 items)
        {
            'name': 'Arduino Uno R3',
            'category': 'ELECTRONICS',
            'material': 'PCB',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.025'),
            'cost_per_unit': Decimal('450.00'),
            'supplier_name': 'Electronics Hub',
            'current_stock': Decimal('40'),
            'min_stock_level': Decimal('10'),
        },
        {
            'name': 'Motor Driver L298N',
            'category': 'ELECTRONICS',
            'material': 'PCB Module',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.035'),
            'cost_per_unit': Decimal('180.00'),
            'supplier_name': 'Electronics Hub',
            'current_stock': Decimal('35'),
            'min_stock_level': Decimal('8'),
        },
        {
            'name': 'Limit Switch Roller Type',
            'category': 'ELECTRONICS',
            'material': 'Plastic Housing',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.045'),
            'cost_per_unit': Decimal('85.00'),
            'supplier_name': 'Electronics Hub',
            'current_stock': Decimal('50'),
            'min_stock_level': Decimal('12'),
        },
        {
            'name': 'Proximity Sensor NPN 12V',
            'category': 'ELECTRONICS',
            'material': 'Metal Body',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.055'),
            'cost_per_unit': Decimal('220.00'),
            'supplier_name': 'Electronics Hub',
            'current_stock': Decimal('28'),
            'min_stock_level': Decimal('6'),
        },
        {
            'name': 'Power Supply 12V 5A',
            'category': 'ELECTRONICS',
            'material': 'SMPS',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.320'),
            'cost_per_unit': Decimal('380.00'),
            'supplier_name': 'Electronics Hub',
            'current_stock': Decimal('22'),
            'min_stock_level': Decimal('5'),
        },
        {
            'name': 'Relay Module 4 Channel',
            'category': 'ELECTRONICS',
            'material': 'PCB',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.065'),
            'cost_per_unit': Decimal('150.00'),
            'supplier_name': 'Electronics Hub',
            'current_stock': Decimal('32'),
            'min_stock_level': Decimal('8'),
        },
        
        # CUSTOM MACHINED PARTS (3 items)
        {
            'name': 'CNC Bracket Type A',
            'category': 'CUSTOM_MACHINED',
            'material': 'Aluminium 6061',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.185'),
            'cost_per_unit': Decimal('280.00'),
            'supplier_name': 'Precision Machining Works',
            'current_stock': Decimal('45'),
            'min_stock_level': Decimal('10'),
        },
        {
            'name': 'Laser Cut Mount Plate',
            'category': 'CUSTOM_MACHINED',
            'material': 'MS 3mm',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.245'),
            'cost_per_unit': Decimal('120.00'),
            'supplier_name': 'Precision Machining Works',
            'current_stock': Decimal('60'),
            'min_stock_level': Decimal('15'),
        },
        {
            'name': 'Coupling Hub 20mm Bore',
            'category': 'CUSTOM_MACHINED',
            'material': 'EN8',
            'unit_type': 'NOS',
            'weight_per_unit': Decimal('0.420'),
            'cost_per_unit': Decimal('350.00'),
            'supplier_name': 'Precision Machining Works',
            'current_stock': Decimal('28'),
            'min_stock_level': Decimal('6'),
        },
    ]
    
    components = []
    for data in components_data:
        component = Component.objects.create(**data)
        components.append(component)
        print(f"  ✓ {component.name}")
    
    print(f"✅ Created {len(components)} components\n")
    return components


def create_projects():
    """Create 5 realistic mechanical projects"""
    print("📁 Creating projects...")
    
    today = date.today()
    
    projects_data = [
        {
            'name': 'Automated Conveyor System',
            'description': 'Design and fabrication of 3-meter automated conveyor belt system with variable speed control and sensor-based object detection for warehouse automation.',
            'client_name': 'TechnoLogistics Pvt Ltd',
            'start_date': today - timedelta(days=45),
            'deadline': today + timedelta(days=30),
            'status': 'IN_PROGRESS',
        },
        {
            'name': 'Mini CNC Machine',
            'description': 'Development of desktop CNC milling machine with 300x300mm work area, NEMA17 stepper motors, and Arduino-based GRBL controller for educational purposes.',
            'client_name': 'Engineering College Lab',
            'start_date': today - timedelta(days=20),
            'deadline': today + timedelta(days=50),
            'status': 'PLANNING',
        },
        {
            'name': 'Solar Panel Cleaning Robot',
            'description': 'Autonomous robot for cleaning solar panels with water spray system, brush mechanism, and edge detection sensors. Designed for rooftop solar installations.',
            'client_name': 'GreenEnergy Solutions',
            'start_date': today - timedelta(days=60),
            'deadline': today + timedelta(days=15),
            'status': 'IN_PROGRESS',
        },
        {
            'name': 'Electric Go-Kart Prototype',
            'description': 'Single-seater electric go-kart with 1HP motor, custom chassis, regenerative braking, and battery management system for college racing competition.',
            'client_name': 'Mechanical Engineering Department',
            'start_date': today - timedelta(days=90),
            'deadline': today - timedelta(days=5),
            'status': 'COMPLETED',
        },
        {
            'name': 'Pick and Place Robotic Arm',
            'description': '4-DOF robotic arm with servo motors, gripper mechanism, and Arduino control for automated sorting and packaging applications in small-scale industries.',
            'client_name': 'AutoMech Robotics Startup',
            'start_date': today - timedelta(days=10),
            'deadline': today + timedelta(days=70),
            'status': 'PLANNING',
        },
    ]
    
    projects = []
    for data in projects_data:
        project = Project.objects.create(**data)
        projects.append(project)
        print(f"  ✓ {project.name} ({project.status})")
    
    print(f"✅ Created {len(projects)} projects\n")
    return projects


def create_bom_items(projects, components):
    """Create realistic BOM items for each project"""
    print("🔩 Creating BOM items...")
    
    # Project 1: Automated Conveyor System
    bom_project1 = [
        (components[23], Decimal('2')),   # AC Motor 1HP
        (components[10], Decimal('4')),   # 6205 Bearing
        (components[2], Decimal('50')),   # M10 Hex Bolt
        (components[7], Decimal('50')),   # Spring Washer M10
        (components[18], Decimal('15')),  # MS Sheet 3mm (kg)
        (components[25], Decimal('2')),   # Motor Driver L298N
        (components[26], Decimal('4')),   # Limit Switch
        (components[27], Decimal('3')),   # Proximity Sensor
    ]
    
    # Project 2: Mini CNC Machine
    bom_project2 = [
        (components[22], Decimal('3')),   # Stepper Motor NEMA17
        (components[12], Decimal('6')),   # Linear Bearing LM8UU
        (components[16], Decimal('3')),   # Linear Shaft 8mm (meters)
        (components[17], Decimal('8')),   # Aluminium Plate 5mm (kg)
        (components[24], Decimal('1')),   # Arduino Uno
        (components[30], Decimal('2')),   # CNC Bracket Type A
        (components[1], Decimal('40')),   # M8 Hex Bolt
        (components[4], Decimal('40')),   # M8 Flat Washer
    ]
    
    # Project 3: Solar Panel Cleaning Robot
    bom_project3 = [
        (components[20], Decimal('4')),   # 12V DC Motor
        (components[8], Decimal('8')),    # 608ZZ Ball Bearing
        (components[24], Decimal('1')),   # Arduino Uno
        (components[25], Decimal('2')),   # Motor Driver L298N
        (components[26], Decimal('4')),   # Limit Switch
        (components[28], Decimal('1')),   # Power Supply 12V
        (components[17], Decimal('5')),   # Aluminium Plate (kg)
        (components[0], Decimal('30')),   # M6 Hex Bolt
    ]
    
    # Project 4: Electric Go-Kart (Completed)
    bom_project4 = [
        (components[23], Decimal('1')),   # AC Motor 1HP
        (components[10], Decimal('4')),   # 6205 Bearing
        (components[18], Decimal('25')),  # MS Sheet 3mm (kg)
        (components[14], Decimal('2')),   # Stainless Steel Shaft 25mm
        (components[2], Decimal('60')),   # M10 Hex Bolt
        (components[3], Decimal('60')),   # M6 Hex Nut
        (components[32], Decimal('4')),   # Coupling Hub
        (components[28], Decimal('1')),   # Power Supply
    ]
    
    # Project 5: Pick and Place Robotic Arm
    bom_project5 = [
        (components[21], Decimal('4')),   # 24V DC Gear Motor
        (components[9], Decimal('4')),    # 6204 Bearing
        (components[24], Decimal('1')),   # Arduino Uno
        (components[29], Decimal('1')),   # Relay Module
        (components[17], Decimal('3')),   # Aluminium Plate (kg)
        (components[30], Decimal('6')),   # CNC Bracket
        (components[1], Decimal('35')),   # M8 Hex Bolt
        (components[6], Decimal('35')),   # Socket Head Cap Screw
    ]
    
    all_bom_data = [
        (projects[0], bom_project1),
        (projects[1], bom_project2),
        (projects[2], bom_project3),
        (projects[3], bom_project4),
        (projects[4], bom_project5),
    ]
    
    bom_count = 0
    for project, bom_items in all_bom_data:
        print(f"\n  📋 {project.name}:")
        for component, quantity in bom_items:
            BOMItem.objects.create(
                project=project,
                component=component,
                quantity_required=quantity
            )
            print(f"    • {component.name} × {quantity}")
            bom_count += 1
    
    print(f"\n✅ Created {bom_count} BOM items\n")
    return bom_count


def main():
    """Main execution function"""
    print("="*60)
    print("🏭 MECHANICAL ERP - DEMO DATA GENERATOR")
    print("="*60)
    print()
    
    # Clear existing data
    clear_existing_data()
    
    # Create components
    components = create_components()
    
    # Create projects
    projects = create_projects()
    
    # Create BOM items (this will auto-create stock transactions via signals)
    bom_count = create_bom_items(projects, components)
    
    # Get transaction count
    transaction_count = StockTransaction.objects.count()
    
    # Summary
    print("="*60)
    print("✅ DEMO DATA SUCCESSFULLY CREATED!")
    print("="*60)
    print(f"\n📊 Summary:")
    print(f"  • Components: {len(components)}")
    print(f"  • Projects: {len(projects)}")
    print(f"  • BOM Items: {bom_count}")
    print(f"  • Stock Transactions: {transaction_count}")
    print()
    print("🌐 You can now access:")
    print("  • Dashboard: http://localhost:8000")
    print("  • Components: http://localhost:8000/components/")
    print("  • Projects: http://localhost:8000/projects/")
    print("  • Analytics: http://localhost:8000/analytics/")
    print()
    print("="*60)

if __name__ == '__main__':
    main()
