# Как запустить

1. Перейти в freewilly/human-violence-scraping/
2. Скачать проект (либо через уставновку git package выполнить команду 'git clone <link>', предварительно получив personal access token или SSH key в настройках github-аккаунта)
3. Будучи в папке human-violence-scraping, запустить Dockerfile, используя команду 'docker build -t animal_scrapper .', и создать image проекта
4. Далее выполнить команду создания контейнера с проектом: docker run -it animal_scrapper
5. В результате получаем ссылку, по которой надо перейти в браузере (должна быть http://127.0.0.1:5000/)
6. На стартовой странице находится кнопка, нажав которую получаем JSON request
