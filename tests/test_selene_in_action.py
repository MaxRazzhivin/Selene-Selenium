from model.data.users import user
from model.pages.registration_page import RegistrationPage


def test_registers_user():
    registration_page = RegistrationPage()
    (registration_page.open()
     .register(user)
     .should_have_registered(user))