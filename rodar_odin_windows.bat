@echo off
cd /d %~dp0
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate
pip install -r requirements.txt
copy /Y .env.example .env >nul
python manage.py migrate
echo.
echo ==========================================
echo Se for a primeira vez, crie o superuser:
echo python manage.py createsuperuser
echo ==========================================
echo.
python manage.py runserver 0.0.0.0:8000
pause
