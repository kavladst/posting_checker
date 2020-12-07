# Posting Checker

## Методы

0. **/api/openapi** - OpenAPI со всеми методами.

1. **/v1/phrase_region/add** - регистрирует поисковую пару в системе по
фразе (phrase) и региону (region).

2. **/v1/phrase_region/** - возвращает все поисковые пары в системе (чтобы
узнать id у пары).

3. **/v1/stat/** - принимает на вход id связки (поисковая фраза + регион)
и интервал (start_date, end_date), за который нужно вывести счётчики.
Возвращает счётчики и соответствующие им временные метки (timestamp).

4. **/v1/stat/update** - принимает на вход id связки (поисковая фраза + регион)
и для него добавляет новую статистку в систему.

5. **/v1/phrase_region/top_posts** - возвращает топ 5 объявления по id связки.

## Запуск

    docker-compose build
    docker-compose up

Приложение запущено на 80 порту. http://localhost/v1/phrase_region/

## Тестирование

    cd posting_api/tests/functional
    docker-compose build
    docker-compose up
