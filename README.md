#### Описание
Данный проект представляет собой сайт резюме с админкой, в которой можно управлять сведениями кандидата: контакты, образование, опыт работы, курсы повышения квалификации. Проект выполнен на `Django` + `Bootsrap`.

Мое резюме - [http://arkuz.pythonanywhere.com](http://arkuz.pythonanywhere.com)
 
 
#### Требования к ПО
- Установленный Python 3.7
- Установленный инструмент для работы с виртуальными окружениями virtualenv
```bash
pip install virtualenv
```

#### Установка
```bash
git clone https://github.com/arkuz/my_django_resume
cd my_django_resume
virtualenv env
env/scripts/activate
pip install -r requirements.txt
```

#### Создание базы данных
База данных по умолчанию - `sqlite3`.

Перейти в папку с файлом менеджера Django `../cd my_django_resume/my_resume/manage.py` и выполнить команды:
```bash
manage.py makemigrations resume
manage.py migrate
```

#### Создание суперпользователя для доступа к админке
```bash
manage.py createsuperuser
```

#### Запуск приложения
```bash
manage.py runserver
```

#### Управление
Логинимся в админку `http://127.0.0.1:8000/admin` с логином и паролем для `superuser`, которого создали выше, и заполняем резюме кандидата. Сайт отображающий резюме доступен по адресу `http://127.0.0.1:8000`.

