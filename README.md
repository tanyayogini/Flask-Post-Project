# Flask-Post-Project
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
  ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
  
Приложение на фласке, в котором можно найти пост по ключевому слову и добавить свой пост:
 - `/` – главная страница (поиск постов)
 - `/search/?s=поиск` – страничка ленты по тегу
 - `GET /post` – страничка добавления поста
 - `POST /post` – страничка после добавления поста

Использована шаблонизация Jinja, при создании поста осуществляется проверка загружаемых файлов. 
