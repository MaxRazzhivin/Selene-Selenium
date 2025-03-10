import os
from selene.support.shared import browser
from selene import have, by, be, command


class RegistrationPage:
    def open(self):
        browser.open('/')

        # Удаляем рекламу
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element("..").click()

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirth').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_tab()

    def fill_hobbies(self, value1, value2):
        browser.all('.custom-checkbox').element_by(have.exact_text(value1)).click()
        browser.all('.custom-checkbox').element_by(have.exact_text(value2)).click()

    def fill_image(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath("../resources/picta.png"))

    def fill_address(self, value):
        browser.element('#currentAddress').click().type(value)

    def fill_state(self, value):
        browser.element('#state').click().element(by.text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click().element(by.text(value)).click()

    def should_registered_user_with(self, full_name, email, gender, mobile, date_of_birth, subject, hobbies, image_name, address,
                                    state_city):
        browser.element(".table").all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subject,
                hobbies,
                image_name,
                address,
                state_city,
        ))

    def button_close_should_be_clickable(self):
        browser.element('#closeLargeModal').should(be.clickable)

    def submit(self):
        browser.element('#submit').perform(command.js.click)






