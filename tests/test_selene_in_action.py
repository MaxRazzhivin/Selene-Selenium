from selene import browser, by, be, have, command
import os


def test_complete_do():
    browser.open('/')

    # Удаляем рекламу
    browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")


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

    browser.element('#uploadPicture').send_keys(os.path.abspath("resources/picta.png"))

    browser.element('#currentAddress').click().type('somewhere in galaxy')

    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    browser.element('#submit').perform(command.js.click)

    browser.element(".table").should(have.text("Max Razzhivin"))
    browser.element(".table").should(have.text("max.nvo06@gmail.com"))
    browser.element(".table").should(have.text("Male"))
    browser.element('.table').should(have.text('9094618666'))
    browser.element('.table').should(have.text('06 April,1989'))
    browser.element('.table').should(have.text('Computer Science'))
    browser.element('.table').should(have.text('Sports, Reading'))
    browser.element('.table').should(have.text('picta.png'))
    browser.element('.table').should(have.text('somewhere in galaxy'))
    browser.element('.table').should(have.text('NCR Delhi'))
    browser.element('#closeLargeModal').should(be.clickable)
