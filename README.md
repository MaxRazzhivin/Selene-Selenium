# Здесь будут заметки по началу изучения Selene 

## Установка Selene
```bash
pip install selene --pre
```

## Пример использования Selene

```bash
from selene import browser, have

browser.open('https://demoqa.com/automation-practice-form')
browser.should(have.title('DEMOQA')) # проверка, что вкладка содержит текст «DEMOQA»

# Элемент по селектору «main-header» должен содержать текст «Box»
browser.element('.main-header').should(have.text('Box'))
```

```bash
Если необходимо обратиться к элементу по атрибуту for="gender-radio-1", то запись будет выглядеть так:

browser.element('[for="gender-radio-1"]')

Все атрибуты записываются в квадратных скобках.
```

## Base URL

```bash
Чтобы не писать полностью путь к странице можно ее основную часть вынести в base_url:

from selene import browser

browser.config.base_url = 'https://demoqa.com' # базовый URL. Данные конфигурации нужно выносить в отдельный файл conftest.py в виде фикстуры

browser.open('/automation-practice-form') # откроется https://demoqa.com/automation-practice-form

Выносить в base_url нужно только те части, которые не будут меняться. Выносить урл в base_url нужно когда у вас много тестов на один и тот же сайт, и чтобы не дублировать код.
```

## Работа с разными браузерами

```bash
По умолчанию Selene использует браузер Chrome. Если нужно использовать другой браузер, то нужно указать его в конфигурации:

Пример для Firefox:

from selene import browser

browser.config.driver_name = 'firefox' 

или 

from selene import browser
from selenium import webdriver

browser.config.driver = webdriver.Firefox()  # или если нужно добавлять специальныи опции то используют `FirefoxOptions()`
```

```bash
Пример для Edge:

from selene import browser

`browser.config.driver_name = 'edge'`

или

browser.config.driver = webdriver.Edge() # или если нужно добавлять специальныи опции то используют `EdgeOptions()`
```

## Поиск одного элемента

```bash
from selene import browser

browser.element('.main-header')

Команда browser.element('селектор') находит только один элемент. Если элементов несколько, то будет найден только первый.

Если нужно обратиться к определенному элементу, что находится внутри другого, то нужно использовать следующую запись:

browser.element('.main-header').element('.sub-header')

Таким образом мы ищем элемент с классом main-header и внутри него ищем элемент с классом sub-header.
```

## Поиск несколько элементов

```bash
from selene import browser

browser.all('.main-header')

Команда browser.all('селектор') находит все элементы, которые соответствуют селектору. Возвращает список элементов. Чтобы обратиться к определенному элементу, нужно добавлять уточнение.

Пример:

from selene import browser

browser.all('.main-header').first.should(have.text('Box')) # обращение к первому элементу и проверяется, что он содержит текст «Box»
```

## Ввод текста в поле

```bash
В Selene ввод текста в поле осуществляется методом type. В этом методе вводится текст, по одной букве(симуляция нажатия клавиш пользователем).

from selene import browser

browser.element('#firstName').type('Иванов Иван')

Если нужно ввести текст сразу, то нужно использовать ввод через js, а именно использовать метод set_value 

from selene import browser

browser.element('#firstName').set_value('Иванов Иван')
```

## Проверки элементов

```bash
Все проверки в Selene начинаются с should. Например, проверка на наличие текста:

from selene import browser, have

browser.element('#firstName').should(have.value('Иванов Иван'))
```

## Опции для браузера

```bash
Пример headless-режима(без отображения окна браузера):

from selene import browser
from selenium import webdriver

driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless')  # вместо этой строки можно добавить другие опции
browser.config.driver_options = driver_options
```

## Время ожидания

```bash
По умолчанию глобальное время ожидания элементов 4 секунды. Если нужно увеличить время ожидания, то нужно указать его в конфигурации:

from selene import browser

browser.config.timeout = 20.0

Если необходимо увеличить время ожидания только для конкретного элемента, то нужно указать его перед командой проверки should:

from selene import browser, have

browser.element('#firstName').with_(timeout=15).should(have.value('Иванов Ива'))

Данное время ожидания будет действовать только для этого элемента и оно главнее глобального.
```

## Команды для работы с элементами

```bash

from selene import browser, command

browser.element('element').perform(command.js.click) # клик по элементу
browser.element('element').perform(command.js.scroll_into_view) # прокрутка до элемента
```

## Изменение масштаба страницы

```bash
from selene import browser

browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'") # уменьшение масштаба страницы до 65%
```

## Загрузка файла

```bash
Ниже приведен пример загрузки файла если есть тег input с атрибутом type="file":

from selene import browser
import os

browser.element('element').send_keys(os.path.abspath('picture.png')) # загрузка файла. Вместо 'picture.png' указать путь к файлу и наименование файла.

Если нет тега input с атрибутом type="file", то нужно использовать метод drop_file из `command.js:

from selene import browser, command
import os

browser.element('element').perform(command.js.drop_file(os.path.abspath('img.png'))) # загрузка файла. Вместо 'img.png' указать путь к файлу и наименование файла.


Путь os.path.abspath('picture.png') указывает на файл, который находится в той же директории, что и тест.

Если нужно более универсальное решение, которое будет находить файл в любой директории запуска теста, то можно использовать следующую запись:

from pathlib import Path


def path(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'resources/{file_name}'))
    
В данном случае файл picture.png находится в директории resources.

Path(file) - это путь к файлу в котором лежит код.
parent.parent - это путь который мы получаем, чтобы добраться от этого файла до корня(до папки, где лежит проект). Количество parent зависит от того, насколько глубоко лежит файл с кодом.
joinpath- это как '+' -добавляем к тому что есть уже путь.
(f'resources/{file_name}') -указываем папку, где лежит файл и переменную для подстановки названия файла. Если файл лежит в корне проекта, то можно убрать 'resources/'.
```

## Работа со слайдером

```bash
Если нужно переместить ползунок в слайдере и нет значение на странице куда именно его переместить, то можно использовать метод drag_and_drop_by_offset из command:

from selene import browser, command

browser.element('element').perform(command.drag_and_drop_by_offset(x=277, y=0)) # перемещение слайдера на 277 пикселей вправо(ось x), если нужно влево, то значение y должно быть отрицательным.

Если на странице есть значение, куда нужно переместить слайдер, то можно использовать метод drag_and_drop_to из command:

from selene import browser, command

browser.element('element').perform(command.drag_and_drop_to('element2'))

Где element - это элемент, который нужно переместить(к примеру это точка на слайдере), а element2 - это элемент, куда нужно переместить.
```

