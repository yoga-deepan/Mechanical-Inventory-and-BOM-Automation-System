# Quick Start Guide - Mechanical ERP

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Start the Server
```bash
python manage.py runserver
```

Visit: **http://localhost:8000**

That's it! The system is ready to use.

---

## 📋 Optional: Background Jobs (Low Stock Alerts)

For automated email alerts, you need Redis and Celery.

### Install Redis

**Windows:** Download from https://github.com/microsoftarchive/redis/releases

**Linux/Mac:**
```bash
sudo apt-get install redis-server  # Ubuntu
brew install redis                  # macOS
```

### Start Redis
```bash
redis-server
```

### Start Celery (in separate terminals)

Terminal 2:
```bash
celery -A mechanical_erp worker -l info
```

Terminal 3:
```bash
celery -A mechanical_erp beat -l info
```

---

## 🎯 First Steps

### 1. Add Your First Component

1. Click **Components** in sidebar
2. Click **Add Component**
3. Fill in:
   - Name: "M8 Bolt"
   - Category: Fasteners
   - Material: "SS304"
   - Unit Type: Numbers
   - Weight per Unit: 0.025 kg
   - Cost per Unit: 0.50
   - Current Stock: 100
   - Min Stock Level: 20
4. Click **Save**

### 2. Create Your First Project

1. Click **Projects** in sidebar
2. Click **Create Project**
3. Fill in:
   - Name: "Hydraulic Press Assembly"
   - Client: "ABC Manufacturing"
   - Start Date: Today
   - Deadline: Next month
   - Status: Planning
4. Click **Save**

### 3. Build a BOM

1. Click **View BOM** on your project
2. Select component: "M8 Bolt"
3. Enter quantity: 50
4. Click **Add to BOM**
5. Watch the totals calculate automatically!
6. Notice stock was deducted from 100 to 50

### 4. View Analytics

1. Click **Analytics** in sidebar
2. See charts showing:
   - Cost distribution
   - Most used components
   - Project status

---

## 🔧 Key Features

### Auto Stock Deduction
When you add a component to BOM, stock is automatically reduced.

### Live Calculator
As you type quantity, cost and weight totals update instantly.

### Low Stock Alerts
Dashboard shows components below minimum stock level.

### Search & Filter
- Components: Search by name, filter by category/material
- Projects: Filter by status, sort by deadline

---

## 📊 Sample Data

Want to test with sample data? Add these components:

| Name | Category | Material | Unit | Weight | Cost | Stock | Min |
|------|----------|----------|------|--------|------|-------|-----|
| M8 Bolt | Fasteners | SS304 | NOS | 0.025 | 0.50 | 100 | 20 |
| 6205 Bearing | Bearings | Steel | NOS | 0.150 | 5.00 | 50 | 10 |
| 20mm Shaft | Shafts | EN8 | METER | 2.500 | 15.00 | 25 | 5 |
| AC Motor 1HP | Motors | - | NOS | 8.500 | 150.00 | 10 | 2 |
| MS Sheet 2mm | Sheet Metal | MS | KG | 1.000 | 3.50 | 200 | 50 |

---

## 🎨 UI Navigation

**Sidebar:**
- Dashboard - Overview and low stock alerts
- Components - Manage inventory
- Projects - Manage projects
- Analytics - View charts and insights

**Top Bar:**
- Shows current page title
- Workshop Control Panel indicator

---

## 💡 Tips

1. **Set realistic min stock levels** - System alerts when stock drops below this
2. **Use descriptive names** - Makes searching easier
3. **Fill in supplier info** - Helps when reordering
4. **Check dashboard daily** - Monitor low stock items
5. **Use filters** - Find components quickly

---

## 🐛 Troubleshooting

**Can't access the site?**
- Make sure server is running: `python manage.py runserver`
- Check URL: http://localhost:8000

**Charts not showing?**
- Check browser console for errors
- Make sure you have data in the system

**Stock not deducting?**
- Check if signals are working
- Look for errors in terminal

---

## 📚 Next Steps

- Read full [README.md](README.md) for detailed documentation
- Access admin panel at `/admin/` (create superuser first)
- Configure email alerts for production use
- Switch to PostgreSQL for production

---

## 🆘 Need Help?

Check the main README.md or create an issue in the repository.

Happy Engineering! 🔧
