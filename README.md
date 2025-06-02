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

# Когда надо перезаписать какой-то параметр из конфига для конкретного элемента - команда .with_()
browser.element('blablabla').with_(timeout=browser.config.timeout*1.5).should(have.size(3))
```

## Небольшая часть аналогий локаторов между Selene и Selenium

```bash
Selene: 
browser.all('#todo-list>li').should(have.size(3)) - поиск списка и проверка на количество элементов == 3

Selenium:
assert len(browser.driver.find_elements(*by.css('todo-list>li'))) == 3 - то же самое, только не хватает еще явного ожидания (Explicite wait)

assert и find_elements - не ждут пока подгрузятся элементы, они сразу кидают ошибку, если элемент не найден, поэтому в Selenium нужны ожидания
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

## Локаторы шпаргалка:


```bash
# open TodoMVC page
browser.open('https://todomvc-emberjs-app.autotest.how/')

# add todos: 'a', 'b', 'c'
browser.element('#new-todo').type('a').press_enter()
browser.element('#new-todo').type('b').press_enter()
browser.element('#new-todo').type('c').press_enter()

# todos should be 'a', 'b', 'c'
browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

# toggle 'b'
browser.all('#todo-list>li').element_by(have.exact_text('b')) \
    .element('.toggle').click()

# completed todos should be 'b'
browser.all('#todo-list>li').by(have.css_class('completed')) \
    .should(have.exact_texts('b'))

# active todos should be 'a', 'c'
browser.all('#todo-list>li').by(have.no.css_class('completed')) \
    .should(have.exact_texts('a', 'c'))
```

## Работа с элементами, которые выделяют массив элементов типа browser.all

```bash
browser.all('#todo-list>li').should(have.size(3))
browser.all('#todo-list>li').first.should(have.exact_text('a'))
browser.all('#todo-list>li').second.should(have.exact_text('b')) - после first и second обращаемся по индексам [2]
browser.all('#todo-list>li')[2].should(have.exact_text('c'))

Либо эти 3 последние строки мы можем записать 1 строкой

browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

Для выбора одного пункта из 3х, найдем один чекбокс из них и кликнем, чтобы отметить 
 
browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()

Проверим, что после клика класс .completed появился только у одного элемента 'b':

browser.all('#todo-list>li').by(have.css_class('completed')).should(have.exact_texts('b'))

Теперь, что остальные элементы остались нетронутые и не приобрели класс .completed: 

browser.all('#todo-list>li').by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))

```

## Обработка плавающих элементов и всплывающих окон, которые могут появиться, а могут и нет: 

```bash
Для этого есть команда .wait_until(condition). Если такой элемент не дождутся, код не упадет с таким wait, а пойдет дальше: 

if browser.element('#crazy_alert_that_appears_sometimes_and_sometimes_not').wait_until(be.visible):
    browser.element('#close_crazy_alert').click()
    
Либо его альтернатива, но без ожидания через .matching(condition):

if browser.matching(have.no.title('TodoMvc')):
    print('Developers went crazy again and screwed up my favourite app title')

```

## Обработка через клавиатуарное сочетание CMD/ctrl + 'A' для выделения всего, например:

```bash
browser.element('#new-todo').type(Keys.COMMAND + 'a' + Keys.NULL)

Keys.NULL - снимает выделение

Для перезаписи текста чем-то другим: 

browser.element('#new-todo').type(Keys.COMMAND + 'a' + Keys.NULL + 'this text will overwrite original text')

либо через команду send_keys() - она позволяет слать больше 1 параметра:

browser.element('#new-todo').send_keys(
    Keys.COMMAND + 'a', 
    Keys.NULL, 
    'this text will overwrite original text')

для ясности чтения кода можно заменить Keys.NULL на release_keys:
    release_keys = Keys.NULL
    browser.element('#new-todo').send_keys(
        Keys.COMMAND + 'a',
        release_keys,
        'this text will overwrite original text',
    ) 
 
```

## Также нам понадобится файл conftest.py для настроек браузера и фикстур
### Файл conftest.py рекомендуется хранить вместе с тестами в одной папке, чтобы он случайно не зааффектил другие файлы, которые начинаются на test...

```bash
import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options
    
    Опциональная настройка, чтобы тесты запускались без открытия браузера
    driver_options.add_argument('--headless')
    
    Опциональная настройка - таймаут для поиска элемента. По-умолчанию 4 секунды стоит
    browser.config.timeout = 2.0
    
    yield
    
    browser.quit()
```

## Пример, если на проекте используется Selenium и как мы можем прикрутить Selene

```bash
Допусти там будет фикстура от Selenium примерно такого вида: 

@pytest.fixture()
def driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )
      
    yield driver
    
    driver.quit()
```

```bash
Тогда мы пишем еще одну фикстуру: 

@pytest.fixture()
def browser(driver):
    
    yield Browser(Config(driver=driver)) - Browser и Config импортируем из Selene

```

```bash
Теперь допустим у нас любой тест на чистом Selenium WebDriver

def test_complete_to_do(driver):
    driver.get('https://todomvc.com/examples/emberjs')
    
    driver.find_element(*by.css('#new-todo')).send_keys('a' + Keys.ENTER)
    driver.find_element(*by.css('#new-todo')).send_keys('b' + Keys.ENTER)
    driver.find_element(*by.css('#new-todo')).send_keys('c' + Keys.ENTER)
    
    
Тогда мы в эту функцию передаем фикстуру для Selene, которую написали выше, и можем постепенно заменять код на код из Selene,
например, заменим нахождение первой строки '#new-todo'

def test_complete_to_do(driver, browser):
    driver.get('https://todomvc.com/examples/emberjs')
    
    browser.element('#new-todo').type('a').press_enter()
    driver.find_element(*by.css('#new-todo')).send_keys('b' + Keys.ENTER)
    driver.find_element(*by.css('#new-todo')).send_keys('c' + Keys.ENTER)
```

## Дополнительные команды через JS с помощью импорт from selene import Command

```bash
Это позволит выполнить ряд команд через perform(command.js. ....)
Например, click или scroll_into_view

Еще помощью JS можно сразу ввести много текста, т.к. Selene по-умолчанию будет вводить посимвольно:
В conftest.py добавляем настройку selene_browser.config.type_by_js = True 

Либо можем настроить не через конфтест, а выборочно для элемента: 
browser.element('#save').with_(click_by_js=True).click()
browser.element('#save').with_(type_by_js=True).type('blablablablablabla')

Подход с кликом через JS полезен, когда нам надо сделать много кликов и мы для этого сохраним в переменной:
save = browser.element('#save').with_(click_by_js=True)
save.click()
save.click()
save.click()
save.click()
save.click()


```
## Как запустить с другими переменными среды из терминала, например, ширина/высота окна браузера или другим url:

```bash
1) conftest.py -> дописываем import os
2) в conftest.py -> по параметрам, которые планируем менять параметры при запуске меняем формат на: 

    browser.config.window_height = os.getenv('window_height', 1680)
    browser.config.window_width = os.getenv('window_width', 1050)
    browser.config.base_url = os.getenv('base_url', 'https://demoqa.com/automation-practice-form')
    browser.config.timeout = os.getenv('timeout', 4.0)

Т.о. если мы запускаем через pytest в терминале без параметров дополнительных, будут отправлены значения по-умолчанию справа

Либо запуск через команду: 

base_url = 'https://todomvc/com' window_height = '900' pytest tests

либо через env -s, это позволит передавать имена через . 

env -s 'base_url = https://todomvc/com window_height = 900' pytest tests

```

## Как зафризить UI на сайте, который пропадает после клика по нему: 

```bash
1) Открываем DevTools на вкладке - Console
2) Выбираем элемент/инпут поле на сайте - который появляется и пропадает
3) Отправляем в консоль команду setTimeout('debugger', 3000) - 3000 мс, это 3 секунды, можно изменить
4) За эти 3 секунды вызываем элемент / поле инпут и он должен зафризиться, можем снять с него корректный локатор
5) Чтобы разморозить, нажимаем на play знак на центре экрана
```



## Настройки для записи экрана при локальных тестах 

```bash
brew install ffmpeg 
```

```bash
import subprocess
import time
from selene import browser

# Функция для начала записи видео
def start_recording():
    command = [
        'ffmpeg',
        '-y',  # перезаписать файл без подтверждения
        '-f', 'x11grab',  # захват экрана / на macOs 'avfoundation'
        '-s', '1920x1080',  # размер экрана / либо разрешение своего экрана
        '-i', ':4',  # входной сигнал (дисплей) / источник видеосигнала для записи
        # источник можно узнать через  'ffmpeg -f avfoundation -list_devices true -i ""', вроде даже экран телефона можно записать через нее
        
        '-c:v', 'libx264',  # кодек
        '-preset', 'ultrafast',  # скорость кодирования
        'output.mp4'  # имя выходного файла
    ]
    return subprocess.Popen(command)

# Функция для остановки записи видео
def stop_recording(process):
    process.terminate()  # Остановить процесс ffmpeg

# Начало записи
video_process = start_recording()
time.sleep(2)  # Небольшая задержка для начала записи

# Ваши тесты
browser.open('https://example.com')
# ... ваши действия с браузером ...

# Остановка записи
stop_recording(video_process)

```

## Как выглядит с conftest из примера: 

```brew
import pytest
from selenium import webdriver
import subprocess
import time
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_height = 1680
    browser.config.window_width = 1050
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 4.0
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options

    # Функция для начала записи видео
    def start_recording():
        command = [
            'ffmpeg',
            '-y',  # перезаписать файл без подтверждения
            '-f', 'avfoundation',  # захват экрана
            '-s', '1680x1050',  # размер экрана
            '-i', '4',  # входной сигнал (дисплей)
            '-c:v', 'libx264',  # кодек
            '-preset', 'ultrafast',  # скорость кодирования
            'output.mp4'  # имя выходного файла
        ]
        return subprocess.Popen(command)

    # Начало записи
    video_process = start_recording()
    time.sleep(2)  # Небольшая задержка для начала записи


    yield

    # Функция для остановки записи видео
    def stop_recording(process):
        process.terminate()  # Остановить процесс ffmpeg

    # Остановка записи
    stop_recording(video_process)

    browser.quit()

```