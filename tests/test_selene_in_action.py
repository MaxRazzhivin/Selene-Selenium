from selene import browser, by, be, have, command
import os


def test_complete_do():
    browser.open('/automation-practice-form')

    # Удаляем рекламу
    browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    # WHEN
    browser.element('#firstName').type('Max')
    browser.element('#lastName').type('Razzhivin')
    browser.element('#userEmail').type('max.nvo06@gmail.com')
    browser.all('[name=gender]').element_by(have.value('Male')).element("..").click()
    browser.element('#userNumber').type('9094618666')

    # Выбираем дату рождения:
    browser.element('#dateOfBirth').click()
    browser.element('.react-datepicker__month-select').type("April")
    browser.element('.react-datepicker__year-select').type("1989")
    browser.element('.react-datepicker__day--006').click()


    # Предметы
    browser.element('#subjectsInput').type('Computer Science').press_tab()

    # Хобби
    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../resources/picta.png')
    ))

    browser.element('#currentAddress').click().type('somewhere in galaxy')

    # Добавил скролл для маленьких экранов до элемента
    browser.element('#state').perform(command.js.scroll_into_view)

    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('.table').all('td').even.should(
        have.texts(
            "Max Razzhivin",
            "max.nvo06@gmail.com",
            "Male",
            '9094618666',
            '06 April,1989',
            'Computer Science',
            'Sports, Reading',
            'picta.png',
            'somewhere in galaxy',
            'NCR Delhi'))
    browser.element('#closeLargeModal').should(be.clickable)
