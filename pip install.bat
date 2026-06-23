@echo off

echo Paketler kuruluyor...

python -m pip install --upgrade pip

pip install -r requirements_full.txt

echo.
echo Kurulum tamamlandi.
pause
