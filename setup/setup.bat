@echo off

IF EXIST venv (
    echo Virtual environment already exists
) ELSE (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Installing requirements...
pip install -r requirements.txt
echo Done installing requirements

echo Making migrations
python manage.py makemigrations
python manage.py migrate