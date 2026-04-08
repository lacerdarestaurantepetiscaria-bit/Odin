@echo off
cd /d %~dp0
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate
pip install -r requirements.txt
if not exist .env copy .env.example .env >nul
python manage.py makemigrations
python manage.py migrate
echo.
echo ==========================================
echo Se ainda nao criou o admin, rode:
echo python manage.py createsuperuser
echo ==========================================
echo.
python manage.py runserver 0.0.0.0:8000
pause
