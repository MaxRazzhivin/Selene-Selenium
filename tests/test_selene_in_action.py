from selene import browser, by, be, have
import os


def test_complete_do():
    browser.open('/')
    browser.driver.execute_script("$('#fixedban').remove()")

    browser.element('#firstName').type('Max')
    browser.element('#lastName').type('Razzhivin')
    browser.element('#userEmail').type('max.nvo06@gmail.com')
    browser.element('label[class=custom-control-label]').click()
    browser.element('[placeholder="Mobile Number"]').type('9094618666')

    # Выбираем дату рождения:
    browser.element('#dateOfBirth').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="3"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1989"]').click()
    browser.element('.react-datepicker__day--006').click()

    # Предметы
    browser.element('#subjectsInput').type('English').press_enter()

    # Хобби
    browser.element('#hobbiesWrapper [for="hobbies-checkbox-1"]').click()
    browser.element('#hobbiesWrapper [for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath("picta.png"))

    browser.element('#currentAddress').click().type('somewhere in galaxy')

    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    browser.element('#submit').click()

    browser.element(".table").should(have.text("Max Razzhivin"))
    browser.element(".table").should(have.text("max.nvo06@gmail.com"))
    browser.element(".table").should(have.text("Male"))
    browser.element('.table').should(have.text('9094618666'))
    browser.element('.table').should(have.text('06 April,1989'))
    browser.element('.table').should(have.text('English'))
    browser.element('.table').should(have.text('Sports, Reading'))
    browser.element('.table').should(have.text('picta.png'))
    browser.element('.table').should(have.text('somewhere in galaxy'))
    browser.element('.table').should(have.text('NCR Delhi'))
    browser.element('#closeLargeModal').should(be.clickable)
