### Homework

Создайте сервер, возвращающий следующие странички:
* по адресу "/hello_world" - страничку с текстом “Привет, мир!”
* по адресу "/cars" - страничку с текстом “Chevrolet, Renault, Ford, Lada”
* по адресу  "/cats" - страничку, на которой написано название одной случайной породы кошек из списка: Корниш рекс, Русская голубая, Шотландская вислоухая, Мэйн-Кун, Манчкин
примечание: чтобы выбрать случайное значение из списка можно воспользоваться функцией choice из модуля random

* url = "/get_time/now", который вернёт строку "Точное время {current_time}" где current_time -- точное текущее время. Чтобы получить точное время можно воспользоваться функцией now() из модуля datetime.datetime

* url = "/get_time/future", который вернёт строку "Точное время через час будет {current_time_after_hour}" где current_time_after_hour -- точное время через 1 час. Чтобы понять сколько времени будет через час, рекомендуется пользоваться модулем datetime.timedelta

* url = "/get_random_word" , в ответе должно быть случайное слово из книги Война и Мир Льва Толстого. Для получения случайного слова можно так же воспользоваться модулем random. При работе endpoint мы должны расчитывать, что книга Война и мир лежит в одной папке с домашним заданием и называется war_and_peace.txt
* Если вы не сделали задание из практики после 3его модуля, сделайте его сейчас: endpoint с url = "/counter", который будет возвращать количество раз, который текущая страничка открывалась. Сделать это вам поможет, например, глобальная переменная (просто объявите переменную счётчик с спецификатором global). Подробнее https://ru.stackoverflow.com/questions/358/Глобальные-переменные-в-python-сохранить-локальную-переменную-от-вызова-к-вызов .
