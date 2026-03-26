# Mechanical Smart Inventory & BOM Manager

A production-quality mini ERP system for managing mechanical component inventory and Bill of Materials (BOM) for engineering projects. Designed for local workshop/lab use without authentication.

## Features

✅ **Component Inventory Management**
- Track mechanical components with categories (Fasteners, Bearings, Shafts, Motors, etc.)
- Real-time stock tracking with engineering precision (DecimalField)
- Search and filter by name, category, and material
- Automatic low stock alerts

✅ **Project & BOM Management**
- Create and manage engineering projects
- Build Bill of Materials dynamically
- Live cost and weight calculation as you type
- Automatic stock deduction when components are added to BOM

✅ **Background Jobs (Celery)**
- Automated low stock email alerts (daily at 9 AM)
- Manual trigger option for immediate checks
- Complete audit trail for all stock transactions

✅ **Analytics Dashboard**
- Cost distribution by category (Pie Chart)
- Most used components (Bar Chart)
- Project status distribution (Doughnut Chart)
- Real-time inventory value tracking

✅ **Professional UI**
- Industrial engineering dashboard theme
- Responsive design with sidebar navigation
- Card-based layout
- Real-time updates without page refresh

## Tech Stack

**Backend:**
- Django 4.2.7
- Django REST Framework
- PostgreSQL (SQLite for development)
- Celery + Redis (background jobs)

**Frontend:**
- HTML5
- CSS3 (Flexbox + Grid)
- Vanilla JavaScript (ES6)
- Chart.js for analytics

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Redis (for Celery background jobs)

**Windows:**
Download from: https://github.com/microsoftarchive/redis/releases

**Linux/Mac:**
```bash
sudo apt-get install redis-server  # Ubuntu/Debian
brew install redis                  # macOS
```

Start Redis:
```bash
redis-server
```

### 3. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit: http://localhost:8000

### 6. Start Celery Worker (in separate terminal)

```bash
celery -A mechanical_erp worker -l info
```

### 7. Start Celery Beat (for scheduled tasks, in separate terminal)

```bash
celery -A mechanical_erp beat -l info
```

## Quick Start Guide

1. **Access Dashboard**: Open http://localhost:8000 in your browser

2. **Add Components**: 
   - Navigate to Components page
   - Click "Add Component"
   - Fill in details (name, category, material, stock, cost, weight)
   - Save

3. **Create Project**:
   - Go to Projects page
   - Click "Create Project"
   - Enter project details (name, client, dates, status)
   - Save

4. **Build BOM**:
   - Click "View BOM" on any project
   - Select component from dropdown
   - Enter quantity required
   - Click "Add to BOM"
   - Watch totals calculate automatically!

5. **Monitor Stock**:
   - Dashboard shows low stock alerts
   - Click "Check Now" to trigger manual email alert
   - View Analytics for insights

## API Endpoints

### Components
- `GET /api/components/` - List all components (supports filters: search, category, material)
- `POST /api/components/` - Create new component
- `PUT /api/components/{id}/` - Update component
- `DELETE /api/components/{id}/` - Delete component

### Projects
- `GET /api/projects/` - List all projects (supports filters: status, sort)
- `POST /api/projects/` - Create new project
- `GET /api/projects/{id}/` - Get project details with BOM
- `PUT /api/projects/{id}/` - Update project
- `DELETE /api/projects/{id}/` - Delete project

### BOM (Bill of Materials)
- `GET /api/bom/?project_id={id}` - Get BOM items for project
- `POST /api/bom/` - Add component to BOM (auto-deducts stock)
- `DELETE /api/bom/{id}/` - Remove item from BOM

### Analytics
- `GET /api/analytics/` - Get dashboard analytics data

### Utilities
- `POST /api/trigger-low-stock/` - Manually trigger low stock check

## Key Features Explained

### 🔩 Auto Stock Deduction
When you add a component to a BOM:
1. System automatically deducts quantity from component stock
2. Creates a stock transaction record (audit trail)
3. Updates project totals instantly
4. Uses Django signals for reliability

### 🚨 Low Stock Email Alerts
- Celery task runs automatically every day at 9 AM
- Checks: `current_stock <= min_stock_level`
- Sends detailed email with component info
- Can be triggered manually from dashboard

### 💰 Live BOM Calculator
JavaScript calculates totals in real-time:
- `Total Cost = quantity × cost_per_unit`
- `Total Weight = quantity × weight_per_unit`
- Grand totals update as you type
- No page refresh needed

### 🎯 Engineering Precision
- Uses `DecimalField` (not FloatField) for accuracy
- Weight precision: 0.001 kg (3 decimal places)
- Cost precision: 0.01 (2 decimal places)
- Perfect for engineering calculations

## Database Models

### Component (Inventory Master)
```python
- name, category, material
- unit_type (NOS/KG/METER)
- weight_per_unit (DecimalField)
- cost_per_unit (DecimalField)
- current_stock, min_stock_level
- supplier_name
```

### Project
```python
- name, description, client_name
- start_date, deadline
- status (PLANNING/IN_PROGRESS/COMPLETED)
- components (ManyToMany through BOMItem)
```

### BOMItem (Through Table)
```python
- project (ForeignKey)
- component (ForeignKey)
- quantity_required (DecimalField)
```

### StockTransaction (Audit Trail)
```python
- component, quantity_changed
- transaction_type (ADDED/USED)
- timestamp, note
```

## Production Deployment

### PostgreSQL Setup

Update `mechanical_erp/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mechanical_erp',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Email Configuration (SMTP)

Update `mechanical_erp/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
ADMIN_EMAIL = 'admin@yourcompany.com'
```

### Static Files

```bash
python manage.py collectstatic
```

## Project Structure

```
mechanical_erp/
├── inventory/              # Main Django app
│   ├── models.py          # Database models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── tasks.py           # Celery tasks
│   ├── signals.py         # Auto stock deduction
│   ├── admin.py           # Admin panel config
│   └── urls.py            # API routes
├── templates/             # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── components.html
│   ├── projects.html
│   ├── project_detail.html
│   └── analytics.html
├── static/
│   ├── css/
│   │   └── style.css      # Industrial theme
│   └── js/
│       └── api.js         # API helpers
├── mechanical_erp/
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   └── celery.py          # Celery config
├── requirements.txt
└── README.md
```

## Admin Panel

Access at `/admin/` with superuser credentials:
- Manage components, projects, BOM items
- View stock transaction history
- Monitor system activity
- Bulk operations

## Troubleshooting

### Redis Connection Error
Make sure Redis is running:
```bash
redis-server
```

### Celery Not Running
Start both worker and beat:
```bash
celery -A mechanical_erp worker -l info
celery -A mechanical_erp beat -l info
```

### Email Not Sending
Check console output (default backend) or configure SMTP settings.

## Future Enhancements

- Unit conversion (Metric ↔ Imperial)
- Export BOM as PDF
- Import components from Excel/CSV
- Barcode scanning support
- Multi-warehouse support
- Purchase order generation

## License

MIT License - Free for commercial and personal use.

## Support

For issues or questions, create an issue in the repository.
