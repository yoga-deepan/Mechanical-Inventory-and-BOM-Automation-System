# Installation Guide - Mechanical ERP

Complete step-by-step installation guide for Windows, Linux, and macOS.

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Redis (optional, for background jobs)

---

## 🪟 Windows Installation

### Step 1: Install Python
Download from: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Step 2: Clone or Download Project
```bash
cd D:\Projects
# Extract the project files here
cd mechanical_erp
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Load Sample Data (Optional)
```bash
python load_sample_data.py
```

### Step 6: Run Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000

### Optional: Install Redis for Background Jobs

1. Download Redis for Windows:
   https://github.com/microsoftarchive/redis/releases

2. Extract and run `redis-server.exe`

3. In new terminals, run:
```bash
# Terminal 2
celery -A mechanical_erp worker -l info

# Terminal 3
celery -A mechanical_erp beat -l info
```

---

## 🐧 Linux Installation (Ubuntu/Debian)

### Step 1: Install Python and pip
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Step 2: Create Virtual Environment (Recommended)
```bash
cd /home/user/projects/mechanical_erp
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Load Sample Data (Optional)
```bash
python load_sample_data.py
```

### Step 6: Run Server
```bash
python manage.py runserver 0.0.0.0:8000
```

Visit: http://localhost:8000

### Optional: Install Redis
```bash
sudo apt install redis-server
sudo systemctl start redis
sudo systemctl enable redis
```

Run Celery:
```bash
# Terminal 2
celery -A mechanical_erp worker -l info

# Terminal 3
celery -A mechanical_erp beat -l info
```

---

## 🍎 macOS Installation

### Step 1: Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Install Python
```bash
brew install python
```

### Step 3: Create Virtual Environment
```bash
cd ~/projects/mechanical_erp
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Load Sample Data (Optional)
```bash
python load_sample_data.py
```

### Step 7: Run Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000

### Optional: Install Redis
```bash
brew install redis
brew services start redis
```

Run Celery:
```bash
# Terminal 2
celery -A mechanical_erp worker -l info

# Terminal 3
celery -A mechanical_erp beat -l info
```

---

## 🐳 Docker Installation (All Platforms)

### Create Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Create docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - redis
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

  celery-worker:
    build: .
    command: celery -A mechanical_erp worker -l info
    depends_on:
      - redis
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0

  celery-beat:
    build: .
    command: celery -A mechanical_erp beat -l info
    depends_on:
      - redis
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
```

### Run with Docker
```bash
docker-compose up
```

---

## 🗄️ PostgreSQL Setup (Production)

### Install PostgreSQL

**Windows:** Download from https://www.postgresql.org/download/windows/

**Linux:**
```bash
sudo apt install postgresql postgresql-contrib
```

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

### Create Database
```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE mechanical_erp;
CREATE USER erp_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE mechanical_erp TO erp_user;
\q
```

### Update settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mechanical_erp',
        'USER': 'erp_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Install PostgreSQL adapter
```bash
pip install psycopg2-binary
```

### Run migrations
```bash
python manage.py migrate
```

---

## 📧 Email Configuration

### For Development (Console)
Already configured in settings.py:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
Emails will print to console.

### For Production (Gmail)

1. Enable 2-factor authentication on Gmail
2. Generate App Password: https://myaccount.google.com/apppasswords

Update settings.py:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
ADMIN_EMAIL = 'admin@yourcompany.com'
```

---

## 🔧 Troubleshooting

### Port 8000 already in use
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

### Redis connection error
Make sure Redis is running:
```bash
# Check if Redis is running
redis-cli ping
# Should return: PONG
```

### Module not found errors
```bash
pip install -r requirements.txt --upgrade
```

### Database errors
```bash
# Delete database and start fresh
rm db.sqlite3
python manage.py migrate
python load_sample_data.py
```

### Static files not loading
```bash
python manage.py collectstatic
```

---

## 🚀 Quick Commands Reference

### Development
```bash
# Start server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Load sample data
python load_sample_data.py

# Run tests
python manage.py test

# Check for issues
python manage.py check
```

### Database
```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database
python manage.py flush

# Database shell
python manage.py dbshell
```

### Celery
```bash
# Start worker
celery -A mechanical_erp worker -l info

# Start beat scheduler
celery -A mechanical_erp beat -l info

# Purge all tasks
celery -A mechanical_erp purge
```

---

## 📊 Verify Installation

After installation, verify everything works:

1. **Server Running**
   - Visit http://localhost:8000
   - Should see dashboard

2. **API Working**
   - Visit http://localhost:8000/api/components/
   - Should see JSON response

3. **Admin Panel**
   - Visit http://localhost:8000/admin/
   - Login with superuser credentials

4. **Sample Data**
   - Check Components page
   - Should see 15 components

5. **Analytics**
   - Visit Analytics page
   - Should see charts

---

## 🎯 Next Steps

1. Read [QUICKSTART.md](QUICKSTART.md) for usage guide
2. Read [README.md](README.md) for full documentation
3. Check [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for technical details

---

## 🆘 Getting Help

If you encounter issues:

1. Check this installation guide
2. Read the troubleshooting section
3. Check Django logs in terminal
4. Verify all dependencies are installed
5. Make sure Redis is running (for Celery)

---

## ✅ Installation Complete!

Your Mechanical ERP system is ready to use.

Start managing your inventory and projects! 🔧
