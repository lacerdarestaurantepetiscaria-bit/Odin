@echo off
cd /d %~dp0
call venv\Scripts\activate
python manage.py bootstrap_admin
pause
