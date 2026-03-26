@echo off
echo ========================================
echo Mechanical ERP Setup Script
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Creating database migrations...
python manage.py makemigrations

echo.
echo Running migrations...
python manage.py migrate

echo.
echo ========================================
echo Setup complete!
echo ========================================
echo.
echo To start the application:
echo.
echo Terminal 1: python manage.py runserver
echo Terminal 2: celery -A mechanical_erp worker -l info
echo Terminal 3: celery -A mechanical_erp beat -l info
echo.
echo Then visit: http://localhost:8000
echo.
echo Optional: Create admin user with 'python manage.py createsuperuser'
echo.
pause
