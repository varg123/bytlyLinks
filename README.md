# Обрезка ссылок с помощью Битли

Получение короткой byt.ly-ссылки, количество посещений по ней.


### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для работы необходим доступ к API Bitly, для этого:
1. Регистрируемся на https://bitly.com/.
2. Заходим в зарегестрированный аккаунт.
3. Генерируем токен. 
Переходим в меню `Settings`->`Advanced Settings`->`OAuth`->`Generic Access Token`. Вводим свой пароль в поле `Password` и кликаем на кнопку `Generate token`.
4. Создаем файл `.env`, в котором делаем запись вида `TOKEN=<ваш_токен>`.


### Пример работы

При запуске указывается обязательный параметр `-l` - ссылка на внешний ресурс или ли bitly-ссылка.

```bash
$ python main.py -l https://yandex.ru
Созданная сокращенная ссылка: http://bit.ly/2JgNCf1
$ python main.py -l bit.ly/2JgNCf1
Сумарное кол-во кликов по ссылке: 1
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
