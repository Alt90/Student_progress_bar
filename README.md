# Student_progress_bar

Проект создан для отслеживания успеваемости студентов группы и выполнение проектов в рамках курса "Технология проектирования ПО".

### Установка

    git clone https://github.com/Alt90/Student_progress_bar.git
    pip install -r requirements.txt
    export DB_server=*something*
    export DB_name=*something*
    export DB_user=*something*
    export DB_password=*something*
    export SECRET_KEY=*something*
    python manage.py migrate
    python manage.py runserver