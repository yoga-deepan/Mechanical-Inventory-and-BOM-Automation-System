# Demo Data Information

## 📊 Two Demo Data Scripts Available

### 1. load_sample_data.py (Basic)
**Quick starter data for testing**

- 15 components
- 3 projects
- 15 BOM items
- Good for quick testing

**Usage:**
```bash
python load_sample_data.py
```

### 2. seed_data.py (Comprehensive) ⭐ RECOMMENDED
**Realistic workshop/manufacturing data**

- 33 components across all categories
- 5 realistic engineering projects
- 40 BOM items with proper quantities
- Auto-generated stock transactions

**Usage:**
```bash
python seed_data.py
```

---

## 🔩 Comprehensive Demo Data Details

### Components (33 items)

**Fasteners (8):**
- M6 Hex Bolt SS304
- M8 Hex Bolt Grade 8.8
- M10 Hex Bolt Grade 10.9
- M6 Hex Nut SS304
- M8 Flat Washer
- Self Tapping Screw 4x25mm
- Socket Head Cap Screw M8
- Spring Washer M10

**Bearings (5):**
- 608ZZ Ball Bearing
- 6204 Deep Groove Bearing
- 6205 Deep Groove Bearing
- Thrust Bearing 51204
- Linear Bearing LM8UU

**Shafts (4):**
- Mild Steel Shaft 20mm
- Stainless Steel Shaft 25mm
- Keyed Shaft 15mm EN8
- Linear Shaft 8mm Hardened

**Sheet Metal (3):**
- Aluminium Plate 5mm 6061
- MS Sheet 3mm
- SS304 Plate 4mm

**Motors (4):**
- 12V DC Motor 100RPM
- 24V DC Gear Motor 60RPM
- Stepper Motor NEMA17
- AC Motor 1HP 1440RPM

**Electronics (6):**
- Arduino Uno R3
- Motor Driver L298N
- Limit Switch Roller Type
- Proximity Sensor NPN 12V
- Power Supply 12V 5A
- Relay Module 4 Channel

**Custom Machined Parts (3):**
- CNC Bracket Type A
- Laser Cut Mount Plate
- Coupling Hub 20mm Bore

---

### Projects (5 realistic engineering projects)

#### 1. Automated Conveyor System (In Progress)
**Client:** TechnoLogistics Pvt Ltd

**BOM (8 items):**
- AC Motor 1HP × 2
- 6205 Bearing × 4
- M10 Hex Bolt × 50
- Spring Washer × 50
- MS Sheet 3mm × 15 kg
- Motor Driver × 2
- Limit Switch × 4
- Proximity Sensor × 3

#### 2. Mini CNC Machine (Planning)
**Client:** Engineering College Lab

**BOM (8 items):**
- Stepper Motor NEMA17 × 3
- Linear Bearing LM8UU × 6
- Linear Shaft 8mm × 3 meters
- Aluminium Plate × 8 kg
- Arduino Uno × 1
- CNC Bracket × 2
- M8 Hex Bolt × 40
- M8 Flat Washer × 40

#### 3. Solar Panel Cleaning Robot (In Progress)
**Client:** GreenEnergy Solutions

**BOM (8 items):**
- 12V DC Motor × 4
- 608ZZ Ball Bearing × 8
- Arduino Uno × 1
- Motor Driver × 2
- Limit Switch × 4
- Power Supply 12V × 1
- Aluminium Plate × 5 kg
- M6 Hex Bolt × 30

#### 4. Electric Go-Kart Prototype (Completed)
**Client:** Mechanical Engineering Department

**BOM (8 items):**
- AC Motor 1HP × 1
- 6205 Bearing × 4
- MS Sheet 3mm × 25 kg
- SS Shaft 25mm × 2 meters
- M10 Hex Bolt × 60
- M6 Hex Nut × 60
- Coupling Hub × 4
- Power Supply × 1

#### 5. Pick and Place Robotic Arm (Planning)
**Client:** AutoMech Robotics Startup

**BOM (8 items):**
- 24V DC Gear Motor × 4
- 6204 Bearing × 4
- Arduino Uno × 1
- Relay Module × 1
- Aluminium Plate × 3 kg
- CNC Bracket × 6
- M8 Hex Bolt × 35
- Socket Head Cap Screw × 35

---

## 🎯 Features Demonstrated

### Realistic Engineering Data
- Proper material specifications (SS304, EN8, 6061)
- Accurate weight calculations
- Industry-standard pricing
- Real supplier names
- Appropriate stock levels

### Complete BOM Examples
- Each project has 8 components
- Realistic quantities
- Mix of fasteners, motors, electronics
- Proper unit types (NOS, KG, METER)

### Auto Stock Deduction
- Stock automatically reduced when BOM created
- Stock transactions logged
- Audit trail maintained

### Project Status Mix
- 2 In Progress
- 2 Planning
- 1 Completed

---

## 📈 What You'll See

### Dashboard
- 5 total projects
- 2 in progress
- Low stock alerts (if any)
- Total inventory value

### Components Page
- 33 components organized by category
- Search and filter functionality
- Stock status indicators
- Supplier information

### Projects Page
- 5 realistic projects
- Different statuses
- Client names
- Deadlines

### Analytics
- Cost distribution across categories
- Most used components
- Project status breakdown

---

## 🔄 Switching Between Demo Data

### Clear and Load Basic Data
```bash
python load_sample_data.py
```

### Clear and Load Comprehensive Data
```bash
python seed_data.py
```

Both scripts automatically clear existing data before loading new data.

---

## 💡 Recommendation

**Use `seed_data.py` for:**
- Demos and presentations
- Testing all features
- Showing realistic scenarios
- Client demonstrations

**Use `load_sample_data.py` for:**
- Quick testing
- Development
- Learning the system

---

## 🎓 Learning Value

The comprehensive demo data shows:
- Real-world component naming
- Proper material specifications
- Realistic project descriptions
- Industry-standard practices
- Complete BOM structures
- Stock management workflows

Perfect for understanding how a real mechanical workshop would use the system!
