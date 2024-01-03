#!/bin/bash

if [ -d "venv" ]; then
    echo "Virtual environment already exists."
else
    echo "Creating virtual environment..."
    python -m venv venv
fi
echo "Installing requirements..."
source venv/bin/activate
pip3 install -r requirements.txt
echo "Done installing requirements"


echo "Making migrations"
python manage.py makemigrations
python manage.py migrate
