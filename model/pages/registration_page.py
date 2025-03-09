import os
from selene import browser, be, have
from model.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.phone_number = browser.element('#userNumber')

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.year = browser.element('.react-datepicker__year-select')
        self.month = browser.element('.react-datepicker__month-select')

        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.all(".custom-control-label")
        self.upload_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')

        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('/')
        browser.element('footer').execute_script('element.remove()')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def select_gender(self, value):
        browser.element(f'[value={value}]').element('..').click()
        return self

    def fill_phone_number(self, value):
        self.phone_number.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.year.type(year)
        self.month.type(month)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        self.subjects_input.type(value).press_enter()
        return self

    def select_hobby(self, value):
        self.hobbies.element_by(have.text(value)).click()
        return self

    def select_picture(self, value):
        self.upload_picture.set_value(os.path.abspath(f'resources/{value}'))
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def fill_state(self, value):
        self.state.click().all("#state div").element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        self.city.click().all("#city div").element_by(have.exact_text(value)).click()
        return self

    def click_submit_button(self):
        self.submit.should(be.visible).click()
        return self

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.year, user.month, user.day)
        self.fill_subject(user.subject)
        self.select_hobby(user.hobby)
        self.select_picture(user.picture)
        self.fill_current_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.click_submit_button()
        return self

    def should_have_registered(self, user: User):
        browser.element('.table').all('td:nth-child(2)').should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day} {user.month},{user.year}',
            user.subject,
            user.hobby,
            user.picture,
            user.address,
            f'{user.state} {user.city}'.strip()))
        return self
