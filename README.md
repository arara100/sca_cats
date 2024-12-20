Технології:
Python 3.x
Django
Django REST Framework
MYsql 

встановіть усі залежності:
pip install -r requirements.txt

Для створення таблиць у базі даних виконайте наступні команди:
python manage.py makemigrations
python manage.py migrate

Доступні ендпоінти:
/api/spycats/{id}: Список всіх котів-агентів (GET), створення нового кота (POST), 
Оновлення інформації(PATCH/PUT), видалення(DELETE)

/api/missions/{id}: Список всіх місій (GET), створення нової місії (POST), 
Оновлення інформації про конкретну місію (PATCH/PUT), видалення(DELETE)

/api/targets/{id}: Список всіх таргетів (GET), створення нового таргету (POST),
Оновлення інформації(PATCH/PUT), видалення(DELETE)

/api/missions/create_with_targets/: Створення місії з таргетами (POST)
